import platform
import subprocess


def main():
    num_terminals = int(input("Enter the number of terminals to open: "))
    num_repetition = int(
        input("How many times do you want to run the test? (Max: 1000): ")
    )

    # Prepare the command to execute
    command = f"python main.py {num_repetition}"
    is_windows = platform.system() == "Windows"

    for i in range(num_terminals):
        if is_windows:
            subprocess.Popen(
                ["cmd", "/c", f"start cmd /c {command}"], shell=True
                # ["cmd", "/c", f"start cmd /k {command}"], shell=True
            )
        else:
            subprocess.Popen(
                ["gnome-terminal", "--", "bash", "-c",
                 f'{command}; exec bash']
            )


if __name__ == "__main__":
    main()
