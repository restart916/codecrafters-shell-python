import sys


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
        elif command == "echo":
            sys.stdout.write(" ".join(args) + "\n")
            sys.stdout.flush()
        else:
            sys.stdout.write(f'{command}: command not found\n')
            sys.stdout.flush()


if __name__ == "__main__":
    main()
