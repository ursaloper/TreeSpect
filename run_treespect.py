import os
import sys
import argparse
import subprocess
from datetime import datetime
from collections import deque
import time

# Configuration
IGNORE_DIRS = ["__pycache__", ".git"]
SCRIPT_NAME = os.path.basename(sys.argv[0])
IGNORE_FILE_PREFIXES = ["treespect_result_", "venv_packages_"]
MAX_DEPTH = 10  # Maximum depth for directory traversal
TIMEOUT = 300  # Timeout in seconds (5 minutes)

def is_venv_directory(path):
    venv_indicators = [
        os.path.join(path, "bin", "python"),
        os.path.join(path, "Scripts", "python.exe"),
        os.path.join(path, "pyvenv.cfg"),
    ]
    return any(os.path.exists(indicator) for indicator in venv_indicators)

def get_venv_packages(venv_path):
    pip_path = os.path.join(venv_path, "bin", "pip")
    if not os.path.exists(pip_path):
        pip_path = os.path.join(venv_path, "Scripts", "pip.exe")

    if os.path.exists(pip_path):
        try:
            result = subprocess.run([pip_path, "freeze"], capture_output=True, text=True, timeout=10)
            return result.stdout.strip().split('\n')
        except subprocess.TimeoutExpired:
            print(f"[WARNING] Timeout while getting packages for {venv_path}")
        except Exception as e:
            print(f"[ERROR] Failed to get packages for {venv_path}: {e}")
    return []

def should_ignore_file(filename):
    return any(filename.startswith(prefix) for prefix in IGNORE_FILE_PREFIXES) or filename == SCRIPT_NAME

def scan_directory(directory, venv_output='count', max_depth=MAX_DEPTH):
    start_time = time.time()
    tree = {"dirs": {}, "files": []}
    stack = deque([(directory, tree, 0)])

    while stack:
        current_dir, current_tree, depth = stack.pop()

        if depth > max_depth:
            current_tree["files"].append("[MAX DEPTH REACHED]")
            continue

        if time.time() - start_time > TIMEOUT:
            print("[WARNING] Timeout reached. Stopping directory scan.")
            break

        try:
            for entry in os.scandir(current_dir):
                if entry.is_dir():
                    if entry.name not in IGNORE_DIRS:
                        if is_venv_directory(entry.path):
                            venv_info = f"[virtual environment] {entry.name}"
                            if venv_output != 'none':
                                packages = get_venv_packages(entry.path)
                                if venv_output == 'count':
                                    venv_info += f" ({len(packages)} packages installed)"
                                elif venv_output == 'names':
                                    package_names = [p.split('==')[0] for p in packages]
                                    venv_info += f" (packages: {', '.join(package_names)})"
                                elif venv_output == 'full':
                                    venv_info += f" (packages: {', '.join(packages)})"
                            current_tree["files"].append(venv_info)
                        else:
                            new_tree = {"dirs": {}, "files": []}
                            current_tree["dirs"][entry.name] = new_tree
                            stack.append((entry.path, new_tree, depth + 1))
                elif entry.is_file():
                    if not should_ignore_file(entry.name):
                        current_tree["files"].append(entry.name)
        except PermissionError:
            current_tree["files"].append("[PERMISSION DENIED]")
        except Exception as e:
            current_tree["files"].append(f"[ERROR: {str(e)}]")

    return tree

def print_tree(tree, prefix="", output_file=None, is_last=True):
    def print_line(line):
        if output_file:
            print(line, file=output_file)
        else:
            print(line)

    files = sorted(tree["files"])
    dirs = list(tree["dirs"].items())

    for i, file in enumerate(files):
        connector = "└── " if i == len(files) - 1 and len(dirs) == 0 else "├── "
        print_line(f"{prefix}{connector}{file}")

    for i, (name, subtree) in enumerate(dirs):
        connector = "└── " if i == len(dirs) - 1 else "├── "
        print_line(f"{prefix}{connector}[dir] {name}")
        new_prefix = prefix + ("    " if i == len(dirs) - 1 else "│   ")
        print_tree(subtree, new_prefix, output_file, i == len(dirs) - 1)

def save_tree_to_file(tree, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            print_tree(tree, output_file=f)
        print(f"\n[INFO] Result successfully saved to file {filename}")
    except IOError as e:
        print(f"[ERROR] Error saving result to file: {e}")

def get_all_venv_packages(directory, include_versions=True, max_depth=MAX_DEPTH):
    venv_packages = {}
    stack = deque([(directory, 0)])
    start_time = time.time()

    while stack:
        current_dir, depth = stack.pop()

        if depth > max_depth or time.time() - start_time > TIMEOUT:
            break

        try:
            for entry in os.scandir(current_dir):
                if entry.is_dir() and entry.name not in IGNORE_DIRS:
                    if is_venv_directory(entry.path):
                        packages = get_venv_packages(entry.path)
                        if not include_versions:
                            packages = [p.split('==')[0] for p in packages]
                        venv_packages[entry.name] = packages
                    else:
                        stack.append((entry.path, depth + 1))
        except PermissionError:
            print(f"[WARNING] Permission denied for directory: {current_dir}")
        except Exception as e:
            print(f"[ERROR] Failed to process directory {current_dir}: {e}")

    return venv_packages

def save_venv_packages(venv_packages, filename):
    if not venv_packages:
        print("[INFO] No virtual environments found. File will not be saved.")
        return

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
    if not venv_packages:
        print("[INFO] No virtual environments found.")
        return

    for venv, packages in venv_packages.items():
        print(f"Virtual environment: {venv}")
        for package in packages:
            print(f"  {package}")
        print()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="TreeSpect - Directory Structure Visualizer")
    parser.add_argument("-rs", "--result-save", action="store_true", help="Save the result to a file")
    parser.add_argument("-vp", "--venv-packages", nargs='?', const='count', choices=['none', 'count', 'names', 'full'],
                        default='count', help="Show installed packages in virtual environments: none, count (default), names, or full")
    parser.add_argument("-vo", "--venv-only", action="store_true",
                        help="Show only virtual environment information without the full tree")
    parser.add_argument("-vps", "--venv-packages-save", nargs='?', const='full', choices=['names', 'full'],
                        help="Save virtual environment packages to a file (default: full)")
    parser.add_argument("-md", "--max-depth", type=int, default=MAX_DEPTH, help=f"Maximum depth for directory traversal (default: {MAX_DEPTH})")
    parser.add_argument("-to", "--timeout", type=int, default=TIMEOUT, help=f"Timeout in seconds (default: {TIMEOUT})")
    args = parser.parse_args()

    current_directory = os.getcwd()
    MAX_DEPTH = args.max_depth
    TIMEOUT = args.timeout

    if args.venv_only or args.venv_packages_save:
        venv_packages = get_all_venv_packages(current_directory, include_versions=(args.venv_packages_save != 'names'), max_depth=MAX_DEPTH)
        if args.venv_only:
            print_venv_packages(venv_packages)
        if args.venv_packages_save:
            if venv_packages:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"venv_packages_{timestamp}.txt"
                save_venv_packages(venv_packages, filename)
            else:
                print("[INFO] No virtual environments found. File will not be saved.")
    else:
        directory_structure = scan_directory(current_directory, args.venv_packages, MAX_DEPTH)
        print_tree(directory_structure)

        if args.result_save:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"treespect_result_{timestamp}.txt"
            save_tree_to_file(directory_structure, filename)
