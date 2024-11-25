import os
import subprocess
import sys

# Allowed commands
ALLOWED_COMMANDS = ["echo", "type", "pwd", "cd"]

# Get the PATH environment variable
PATH_ENV = os.environ.get("PATH", "")

def main():
    while True:  # Keep the shell running in a loop
        # Display the shell prompt
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Read user input
        user_command = input().strip()

        # Exit command
        if user_command == "exit 0":
            break

        # Parse the command and arguments
        command_parts = user_command.split()
        base_command = command_parts[0] if command_parts else ""

        command_path = handle_directory_search(base_command)
        if command_path:
            executeProgram(command_path,command_parts[1:])

        # Check if the command is not in the allowed commands
        elif base_command not in ALLOWED_COMMANDS:
            print(f"{base_command}: command not found")
        else:
            if base_command == "echo":
                handle_echo(command_parts[1:])
            elif base_command == "type":
                handle_type(command_parts[1:])
            elif base_command == "pwd":
                handle_pwd()
            elif base_command == "cd":
                handle_cd(command_parts[1:])
                handle_pwd()


def handle_echo(args):
    """Handle the echo command."""
    print(" ".join(args))


def handle_type(args):
    """Handle the type command."""
    if not args:
        print("type: missing argument")
        return

    command = args[0]

    # Check if the command is a shell builtin
    if command == "exit" or command in ALLOWED_COMMANDS:
        print(f"{command} is a shell builtin")
    else:
        # Search for the command in directories
        result = handle_directory_search(command)
        if result:
            print(f"{command} is {result}")
        else:
            print(f"{command}: not found")

def handle_directory_search(cmd):
    """Search for a command in the PATH directories."""
    directories = PATH_ENV.split(":")
    for directory in directories:
        command_path = os.path.join(directory, cmd)
        if os.path.isfile(command_path) and os.access(command_path, os.X_OK):
            return command_path  # Return the full path if command is found
    return None  # Command not found

def executeProgram(program_path, args=[]):
    try:
        result = subprocess.run([program_path, *args])
        return result
    except FileNotFoundError:
        print(f"{program_path}: Command not found")
    except PermissionError:
        print(f"{program_path}: Permission denied")
    except Exception as e:
        print(f"Error executing {program_path}: {e}")

def handle_pwd():
    cwd = os.getcwd()
    print(cwd)

def handle_cd(directory):
    print(directory)
    if directory == "./":
        print("do something")
    elif directory == "../":
        print("do something")
    elif directory == "./dir":
        print("do something")
    elif directory == "~":
        print("do something")
    else:
        os.chdir('directory')

if __name__ == "__main__":
    main()
