import os
import platform
import subprocess


def main():
    num_terminals = int(input("Enter the number of terminals to open: "))
    num_repetition = int(
        input("How many times do you want to run the test? (Max: 1000)")
    )

    command = "python main.py"
    answer = num_repetition

    is_windows = platform.system() == "Windows"

    for i in range(num_terminals):
        if is_windows:
            subprocess.Popen(
                ["start", "cmd", "/k", f"{command} && echo {answer}"], shell=True
            )
        else:
            subprocess.Popen(
                ["gnome-terminal", "--", "bash", "-c",
                 f'{command} <<< "{answer}"; exec bash']
            )


if __name__ == "__main__":
    main()
