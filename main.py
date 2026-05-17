import os
import argparse
import sys
from dotenv import load_dotenv
from prompts import *
from functions.call_functions import *

from google import genai
from google.genai import types


def generate_content(client, messages):

    return client.models.generate_content( #Request content generating. Two arguments needed. The model and the prompt. Generate a response with the text atribute.
        model = "gemini-2.5-flash",
        contents = messages,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            tools=[available_functions],
            #temperature=0
            ),
    )
    



load_dotenv() #Load the env variable from .env file


def main():
    api_key = os.environ.get("GEMINI_API_KEY") #Get the api_key from .env

    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY is missing or empty")

    client = genai.Client(api_key=api_key)  #Create a client with the api_key. I will use it to create requests.

    parser = argparse.ArgumentParser(description="chatbot")
    # Create a parser object to handle command-line arguments.
    # The description is shown when using --help.

    parser.add_argument("user_prompt", type=str, help="User prompt")
    # Define a required positional argument called "user_prompt".
    # The value entered in the terminal will be converted to string.
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    # Define an optional command-line flag called --verbose.
    # If the flag is present when running the script, args.verbose will be True.
    # If the flag is not present, args.verbose will be False.
    # This is used to enable or disable verbose (detailed) output in the program.

    args = parser.parse_args()
    # Read and parse the command-line arguments entered by the user.
    # Store them inside the "args" object.

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    # Initialize the conversation history with the first user message.
    # In the future, this list will store the full chat history (user + model messages)
    # so the AI keeps context across multiple turns in the conversation.

    # Run the agent loop with a maximum of 20 iterations
    for _ in range(20):
        
        # Call the model with the current conversation history
        response = generate_content(client, messages)

        # If the model returned candidates, append all of them to the message history
        # (usually there is only one, but the API supports multiple)
        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)

        # Ensure the response contains usage metadata (token information)
        if response.usage_metadata is None:
            raise RuntimeError("Invalid or incomplete Gemini response")

        # Optional debug logging of token usage
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

        # Prepare a list to store tool/function execution results for this iteration
        function_results = []

        # If the model requested function/tool calls, execute them
        if response.function_calls is not None:
            
            for function_call in response.function_calls:
                function_call_result = call_function(function_call, args.verbose)

                # Validate function call result structure
                if not function_call_result.parts:
                    raise Exception("Error: function_call_result.parts is empty")
                if function_call_result.parts[0].function_response is None:
                    raise Exception("Error: function_call_result.parts[0].function_response is None")
                if function_call_result.parts[0].function_response.response is None:
                    raise Exception("Error: function_call_result.parts[0].function_response.response is None")

                # Store validated tool result
                function_results.append(function_call_result.parts[0])

                # Optional debug output for tool results
                if args.verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")

        else:
            # If no function calls are requested, we assume this is the final answer
            print(response.text)
            return

        # Add tool results back into the conversation as user/context messages
        messages.append(types.Content(role="user", parts=function_results))

    # If we reach here, the model never produced a final answer within the iteration limit
    print("Error: the agent exceeded the maximum number of iterations without producing a final answer.")
    sys.exit(1)


if __name__ == "__main__":
    main()
