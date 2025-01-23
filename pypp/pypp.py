import argparse
import os
import tempfile


class PyPP:
    def __init__(self):
        self.in_delete_block = False

    def preprocess_file(self, filepath: str, verbose: bool = False):

        modified = False
        temp_fd, temp_path = tempfile.mkstemp()

        try:
            with open(filepath, "r") as src, os.fdopen(temp_fd, "w") as dst:
                for line in src:
                    if "#PYPP#DELETE#" in line:
                        modified = True
                        if verbose:
                            print(line)
                        continue
                    if "#PYPP#BEGIN#" in line:
                        self.in_delete_block = True
                        modified = True
                        if verbose:
                            print(line)
                        continue
                    if "#PYPP#END#" in line:
                        self.in_delete_block = False
                        modified = True
                        if verbose:
                            print(line)
                        continue
                    if not self.in_delete_block:
                        dst.write(line)  # Write line only if not in delete mode
                    elif verbose:
                        print(line)

            if modified:
                os.replace(temp_path, filepath)
            else:
                os.remove(temp_path)

            if verbose:
                print(f"Processed: {filepath}")

        except Exception as e:
            os.remove(temp_path)
            print(f"Error processing {filepath}: {e}")

    def preprocess_path(self, path: str, recursive: bool = False, verbose: bool = True):
        if os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    if file.endswith(".py"):
                        self.preprocess_file(os.path.join(root, file), verbose)
                if not recursive:
                    break
        else:
            self.preprocess_file(path, verbose)

def main():
    parser = argparse.ArgumentParser(description="Python PreProcessor (PyPP)")
    parser.add_argument("paths", nargs="+", help="Files or directories to preprocess")
    parser.add_argument("--recursive", "-r", action="store_true", help="Process directories recursively")
    parser.add_argument("--verbose", "-v", action="store_true", help="Output removed lines to stdout")
    args = parser.parse_args()

    preprocessor = PyPP()
    for path in args.paths:
        preprocessor.preprocess_path(path, args.recursive, args.verbose)

if __name__ == "__main__":
    main()
