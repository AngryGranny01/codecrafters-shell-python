import os
import sys

# Allowed commands
allowed_commands = ["echo", "type"]

path_env = os.environ.get("PATH")
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

        command_parts = user_command.split()
        base_command = command_parts[0] if command_parts else ""

        # Check if the command is not in the allowed commands
        if base_command not in allowed_commands:
            print(f"{user_command}: command not found")
        else:
            if base_command == "echo":
                handle_echo(command_parts[1:])
            if base_command == "type":
                handle_type(command_parts[1:])
            
def handle_echo(args):
    print(" ".join(args))


def handle_type(args):
    test_type = args[0]
    if(test_type == "exit" or test_type in allowed_commands):
        print(f"{test_type} is a shell builtin")
    else:
        # Search for the command in directories
        result = handle_directory_search(test_type)
        if result:
            print(result)
        else:
            print(f"{test_type}: not found")
            

def handle_directory_search(cmd):
    directories = path_env.split(":")
    for directory in directories:
        execFile = directory.split("/")
        if(execFile == cmd):
            print("/".join(directory))
            return directory

if __name__ == "__main__":
    main()
