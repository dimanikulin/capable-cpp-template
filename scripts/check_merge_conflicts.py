# This script scans files in a directory for Git merge conflict markers.
# It can be used to check for unresolved merge conflicts in code files.
import os
import sys

MERGE_CONFLICT_MARKERS = ['<<<<<<<', '=======', '>>>>>>>']

def find_merge_conflicts_in_file(filepath):
    conflicts = []
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        for lineno, line in enumerate(file, start=1):
            for marker in MERGE_CONFLICT_MARKERS:
                if marker in line:
                    conflicts.append((lineno, marker, line.strip()))
    return conflicts

def scan_directory_for_conflicts(directory, file_extensions=None):
    conflicts_found = {}
    for root, _, files in os.walk(directory):
        for filename in files:
            if file_extensions and not filename.endswith(tuple(file_extensions)):
                continue
            filepath = os.path.join(root, filename)
            conflicts = find_merge_conflicts_in_file(filepath)
            if conflicts:
                conflicts_found[filepath] = conflicts
    return conflicts_found

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Find Git merge conflict symbols in code files.")
    parser.add_argument("path", help="Directory or file to scan")
    parser.add_argument("--ext", nargs='*', help="Limit to specific file extensions, e.g., --ext .py .cpp .js")

    args = parser.parse_args()

    conflict_detected = False

    if os.path.isfile(args.path):
        result = find_merge_conflicts_in_file(args.path)
        if result:
            conflict_detected = True
            print(f"\nMerge conflicts found in: {args.path}")
            for line in result:
                print(f"  Line {line[0]}: {line[1]} -> {line[2]}")
    else:
        result = scan_directory_for_conflicts(args.path, args.ext)
        if result:
            conflict_detected = True
            for file, conflicts in result.items():
                print(f"\nMerge conflicts found in: {file}")
                for line in conflicts:
                    print(f"  Line {line[0]}: {line[1]} -> {line[2]}")

    if conflict_detected:
        print("\nX Merge conflict markers found.")
        sys.exit(1)
    else:
        print("\nV No merge conflicts found.")
        sys.exit(0)
