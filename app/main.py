import os
import sys


commands = {
    "echo": {
        "func": lambda args: " ".join(args),
    },
    "exit": {
        "func": lambda args: args[0],
    },
    "pwd": {
        "func": lambda args: os.getcwd(),
    },
    "cd": {
        "func": lambda args: cd_command(args), 
    },
    "type": {
        "func": lambda args: type_command(args),
    }
}

def cd_command(args):
    try:
        os.chdir(args[0])
    except FileNotFoundError:
        return f"cd: {args[0]}: No such file or directory"
    return None

def type_command(args):
    paths = os.environ.get("PATH")
    paths = paths.split(":")

    command = args[0]
    if command in commands:
        return f"{command} is a shell builtin"
    elif find_path(command):
        return f"{command} is {find_path(command)}/{command}"
    return f"{command}: not found"

def find_path(command):
    paths = os.environ.get("PATH")
    paths = paths.split(":")

    for path in paths:
        if os.path.exists(f"{path}/{command}"):
            return path
    return None

def main():
    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        input_command = input()
        command = input_command.split(" ")[0]
        args = input_command.split(" ")[1:]

        if command == "exit":
            return args[0] if len(args) > 0 else 0
        elif command in commands:
            result = commands[command]["func"](args)
            if result:
                sys.stdout.write(result + "\n")
            sys.stdout.flush()
        elif find_path(command):
            os.system(input_command)
        else:
            sys.stdout.write(f'{command}: command not found\n')
            sys.stdout.flush()


if __name__ == "__main__":
    main()
