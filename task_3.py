import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)


def print_directory_structure(directory: Path, indent: str = ""):
    try:
        for entry in sorted(directory.iterdir()):
            if entry.is_dir():
                print(Fore.BLUE + f"{indent}{entry.name}/")
                print_directory_structure(entry, indent + "    ")
            else:
                print(Fore.GREEN + f"{indent}{entry.name}")
    except PermissionError:
        print(Fore.RED + f"{indent}[Відмовлено в доступі]")


def main():
    if len(sys.argv) < 2:
        print(Fore.RED + "Помилка. Використання: python hw03.py <шлях до директорії>")
        return

    path = Path(sys.argv[1])

    if not path.exists():
        print(Fore.RED + "Помилка: Вказаний шлях не існує.")
        return
    if not path.is_dir():
        print(Fore.RED + "Помилка: Вказаний шлях не є директорією.")
        return

    print(Fore.BLUE + f"{path.name}/")
    print_directory_structure(path, indent="    ")


if __name__ == "__main__":
    main()
