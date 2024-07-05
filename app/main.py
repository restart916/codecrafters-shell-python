import sys


commands = {
    "echo": {
        "func": lambda args: " ".join(args),
    },
    "exit": {
        "func": lambda args: args[0],
    },
    "type": {
        "func": lambda args: type_command(args),
    }
}

def type_command(args):
    command = args[0]
    if command in commands:
        return f"{command} is a shell builtin"
    else:
        return f"{command}: not found"
    

def main():
    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        input_command = input()
        command = input_command.split(" ")[0]
        args = input_command.split(" ")[1:]

        if command == "exit":
            return args[0]
        elif command in commands:
            result = commands[command]["func"](args)
            sys.stdout.write(result + "\n")
            sys.stdout.flush()
        else:
            sys.stdout.write(f'{command}: command not found\n')
            sys.stdout.flush()


if __name__ == "__main__":
    main()
