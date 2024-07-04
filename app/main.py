import sys


def main():
    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command = input()
        if command == "exit 0":
            return 0

        sys.stdout.write(f'{command}: command not found\n')
        sys.stdout.flush()


if __name__ == "__main__":
    main()
