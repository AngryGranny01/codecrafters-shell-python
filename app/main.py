import sys


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

        # Allowed commands (empty in this stage as we handle only missing commands)
        allowed_commands = ["echo"]

        command_parts = user_command.split()
        base_command = command_parts[0] if command_parts else ""

        # Check if the command is not in the allowed commands
        if base_command not in allowed_commands:
            print(f"{user_command}: command not found")
        else:
            if base_command == "echo":
                handle_echo(command_parts[1:])
            

def handle_echo(args):
    print(" ".join(args))

if __name__ == "__main__":
    main()
