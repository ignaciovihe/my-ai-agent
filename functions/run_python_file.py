import os
import subprocess

from google.genai import types


def run_python_file(working_directory, file_path, args=None):
    
    try:
    
        working_directory_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_directory_abs, file_path))
        valid_target_file = os.path.commonpath([working_directory_abs, target_file]) == working_directory_abs

        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not target_file.lower().endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_file]
        if args is not None:
            command.extend(args)

        result = subprocess.run(
            command,
            cwd=working_directory_abs,
            capture_output=True,
            text=True,
            timeout=30
        )

        str_result= ""
        if result.returncode != 0:
            str_result += f"* Process failed with code {result.returncode}"
        else:
            str_result += f"* Process exited with code {result.returncode}\n"
        if not result.stdout and not result.stderr:
            str_result += "* No output produced\n"
        if result.stdout:
            str_result += f"* STDOUT: {result.stdout}\n"
        if result.stderr:
            str_result += f"* STDERR: {result.stderr}\n"
        
        return str_result
        
    except Exception as e:
        return f"Error: executing Python file: {e}"
    


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file located within the working directory, optionally passing command-line arguments, and returns the process output including stdout, stderr, and exit code information",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional list of command-line arguments to pass to the Python script",
                items=types.Schema(
                    type=types.Type.STRING,
                    description="A single command-line argument",
                ),
            ),
        },
        required=["file_path"]
    ),
)