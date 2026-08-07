import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)

def print_directory_structure(directory, indent=""):
  for entry in directory.iterdir():
    if entry.is_dir():
      print(Fore.BLUE + f"{indent}📁 {entry.name}")
      print_directory_structure(entry, indent + "  ")
    else:
      print(Fore.GREEN + f"{indent}📄 {entry.name}")
if __name__ == "__main__":
  path = Path(sys.argv[1])
  print_directory_structure(path)
