import os
import sys
import argparse
import subprocess
from datetime import datetime

# Configuration
IGNORE_DIRS = ["__pycache__"]  # Directories to always ignore
SCRIPT_NAME = os.path.basename(sys.argv[0])
IGNORE_FILE_PREFIXES = ["treespect_result_", "venv_packages_"]

def is_venv_directory(path):
    """Check if the given path is a Python virtual environment."""
    venv_indicators = [
        os.path.join(path, "bin", "python"),
        os.path.join(path, "Scripts", "python.exe"),  # for Windows
        os.path.join(path, "pyvenv.cfg"),
    ]
    return any(os.path.exists(indicator) for indicator in venv_indicators)

def get_venv_packages(venv_path):
    """Get installed packages in the virtual environment."""
    pip_path = os.path.join(venv_path, "bin", "pip")
    if not os.path.exists(pip_path):
        pip_path = os.path.join(venv_path, "Scripts", "pip.exe")  # for Windows

    if os.path.exists(pip_path):
        result = subprocess.run([pip_path, "freeze"], capture_output=True, text=True)
        return result.stdout.strip().split('\n')
    return []

def should_ignore_file(filename):
    """Check if the file should be ignored based on its name."""
    return any(filename.startswith(prefix) for prefix in IGNORE_FILE_PREFIXES) or filename == SCRIPT_NAME

def scan_directory(directory, venv_output='count'):
    """Scan the directory and create a tree structure."""
    tree = {"dirs": {}, "files": []}

    for root, dirs, files in os.walk(directory, topdown=True):
        path = root.replace(directory, '').split(os.sep)
        path = [p for p in path if p]  # Remove empty strings

        current = tree
        for part in path:
            current = current["dirs"].setdefault(part, {"dirs": {}, "files": []})

        for d in dirs:
            if d not in IGNORE_DIRS:
                if is_venv_directory(os.path.join(root, d)):
                    venv_info = f"[virtual environment] {d}"
                    packages = get_venv_packages(os.path.join(root, d))
                    if venv_output == 'count':
                        venv_info += f" ({len(packages)} packages installed)"
                    elif venv_output == 'names':
                        package_names = [p.split('==')[0] for p in packages]
                        venv_info += f" (packages: {', '.join(package_names)})"
                    elif venv_output == 'full':
                        venv_info += f" (packages: {', '.join(packages)})"
                    current["files"].append(venv_info)
                else:
                    current["dirs"][d] = {"dirs": {}, "files": []}

        for file in files:
            if not should_ignore_file(file):
                current["files"].append(file)

        # Exclude ignored directories and virtual environments from further scanning
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not is_venv_directory(os.path.join(root, d))]

    return tree

def print_tree(tree, prefix="", output_file=None):
    """Print the directory tree structure."""
    def print_line(line):
        if output_file:
            print(line, file=output_file)
        else:
            print(line)

    # Print files first
    files = sorted(tree["files"])
    for i, file in enumerate(files):
        if i == len(files) - 1 and len(tree["dirs"]) == 0:
            print_line(f"{prefix}└── {file}")
        else:
            print_line(f"{prefix}├── {file}")

    # Then print directories
    dirs = list(tree["dirs"].items())
    for index, (name, subtree) in enumerate(dirs):
        if index == len(dirs) - 1:
            print_line(f"{prefix}└── [dir] {name}")
            print_tree(subtree, prefix + "    ", output_file)
        else:
            print_line(f"{prefix}├── [dir] {name}")
            print_tree(subtree, prefix + "│   ", output_file)

def save_tree_to_file(tree, filename):
    """Save the tree structure to a file."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            print_tree(tree, output_file=f)
        print(f"\n[INFO] Result successfully saved to file {filename}")
    except IOError as e:
        print(f"[ERROR] Error saving result to file: {e}")

def get_all_venv_packages(directory, include_versions=True):
    """Get all virtual environment packages in the directory."""
    venv_packages = {}
    for root, dirs, _ in os.walk(directory):
        for d in dirs:
            if is_venv_directory(os.path.join(root, d)):
                packages = get_venv_packages(os.path.join(root, d))
                if not include_versions:
                    packages = [p.split('==')[0] for p in packages]
                venv_packages[d] = packages
    return venv_packages

def save_venv_packages(venv_packages, filename):
    """Save virtual environment packages to a file."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for venv, packages in venv_packages.items():
                f.write(f"Virtual environment: {venv}\n")
                for package in packages:
                    f.write(f"  {package}\n")
                f.write("\n")
        print(f"\n[INFO] Virtual environment packages successfully saved to file {filename}")
    except IOError as e:
        print(f"[ERROR] Error saving virtual environment packages to file: {e}")

def print_venv_packages(venv_packages):
    """Print virtual environment packages."""
    for venv, packages in venv_packages.items():
        print(f"Virtual environment: {venv}")
        for package in packages:
            print(f"  {package}")
        print()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="TreeSpect - Directory Structure Visualizer")
    parser.add_argument("-rs", "--result-save", action="store_true",
                        help="Save the result to a file")
    parser.add_argument("-vp", "--venv-packages", nargs='?', const='count', choices=['count', 'names', 'full'],
                        help="Show installed packages in virtual environments: count (default), names, or full")
    parser.add_argument("-vo", "--venv-only", action="store_true",
                        help="Show only virtual environment information without the full tree")
    parser.add_argument("-vps", "--venv-packages-save", nargs='?', const='full', choices=['names', 'full'],
                        help="Save virtual environment packages to a file (default: full)")
    args = parser.parse_args()

    current_directory = os.getcwd()

    if args.venv_only or args.venv_packages_save:
        venv_packages = get_all_venv_packages(current_directory, include_versions=(args.venv_packages_save != 'names'))
        if args.venv_only:
            print_venv_packages(venv_packages)
        if args.venv_packages_save:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"venv_packages_{timestamp}.txt"
            save_venv_packages(venv_packages, filename)
    else:
        venv_output = args.venv_packages if args.venv_packages else 'count'
        directory_structure = scan_directory(current_directory, venv_output)
        print_tree(directory_structure)

        if args.result_save:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"treespect_result_{timestamp}.txt"
            save_tree_to_file(directory_structure, filename)
