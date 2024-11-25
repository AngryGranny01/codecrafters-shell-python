import sys


def main():
    while True:  # Keep the shell running in a loop
        # Display the shell prompt
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Read user input
        user_command = input()

        # Allowed commands (empty in this stage as we handle only missing commands)
        allowed_commands = ["exit 0", "echo"]


        # Check if the command is not in the allowed commands
        if user_command not in allowed_commands:
            print(f"{user_command}: command not found")
        else:
            if user_command == "exit 0":
                break
            commands(user_command) # Exit loop if the command is valid (not required in this stage)

def commands(command):
    match command:
        case "echo":
            print(f"{command[5:]}\n") 
        case _:
            return "Something's wrong with the internet"

if __name__ == "__main__":
    main()
