import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)


def print_directory_structure(directory, indent=""):
    for entry in directory.iterdir():
        if entry.is_dir():
            print(Fore.BLUE + f"{indent}📁 {entry.name}")
            print_directory_structure(entry, indent + "    ")
        else:
            print(Fore.GREEN + f"{indent}📄 {entry.name}")


def main():
    if len(sys.argv) < 2:
        print(Fore.RED + "Використання: python task_3.py <шлях до директорії>")
        return

    path = Path(sys.argv[1])

    if not path.exists():
        print(Fore.RED + "Шлях не існує.")
    elif not path.is_dir():
        print(Fore.RED + "Це не директорія.")
    else:
        print_directory_structure(path)


if __name__ == "__main__":
    main()
