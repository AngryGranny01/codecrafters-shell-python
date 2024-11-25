import os
import sys

# Allowed commands
allowed_commands = ["echo", "type"]

def main():
    while True:  # Keep the shell running in a loop
        # Display the shell prompt
        sys.stdout.write("$ ")
        sys.stdout.flush()

        path_env = os.environ.get("PATH", "")
        print(path_env)
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
    test_command = args[0]
    if(test_command == "exit" or test_command in allowed_commands):
        print(f"{test_command} is a shell builtin")
    
    else:
        print(f"{test_command}: not found")

def handle
if __name__ == "__main__":
    main()
