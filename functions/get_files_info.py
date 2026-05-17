import os # Import OS module to work with file system paths and directories
from google.genai import types 


def get_target_dir_info(target_dir):
    
    items_data = dict()  # Create dictionary to store file/folder metadata
    items = os.listdir(target_dir)  # Get list of items in the target directory

    for item in items:
        full_path = os.path.join(target_dir, item)  # Build full path for each item (required for correct checks and size)
        items_data[item] = {
            "size": os.path.getsize(full_path),  # Get file size using full path
            "is_dir": os.path.isdir(full_path)   # Check if item is a directory
        }

    return items_data  # Return dictionary with all collected metadata


def format_target_dir_info(info):
    lines = []  # List to store formatted output lines

    for key, value in info.items():
        line = f"{key}: file_size={value['size']}, is_dir={value['is_dir']}"  # Format each item as a readable string
        lines.append(line)  # Add formatted line to list

    return "\n".join(lines)  # Join all lines into a single string separated by newlines


def get_files_info(working_directory, directory="."):
    # validate the requested directory

    try:

        working_dir_abs = os.path.abspath(working_directory)  
        # Convert working_directory to absolute path (sandbox root)

        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))  
        # Build target path and normalize it (remove .., ., etc.)

        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs  
        # Ensure target_dir is inside allowed working directory (security check)

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'  
            # Block attempts to escape sandbox

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'  
            # Ensure target is actually a directory

        items_data = get_target_dir_info(target_dir)  
        # Collect metadata for all items in directory

        return format_target_dir_info(items_data)  
        # Convert metadata dictionary into formatted string output

    except ValueError as e:
        return f"Error: {e}"  
        # Handle invalid path operations

    except OSError as e:
        return f"Error: {e}"  
        # Handle filesystem-related errors (permissions, missing files, etc.)

    except Exception as e:
        return f"Error: {e}"  
        # Catch-all for unexpected errors


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)
