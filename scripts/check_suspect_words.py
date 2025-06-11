# This script scans files in a directory for Git merge conflict markers.
# It can be used to check for unresolved merge conflicts in code files.
import os
import sys

def load_conflict_markers(marker_file_path):
    try:
        with open(marker_file_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Error reading marker file: {e}")
        sys.exit(2)

def find_merge_conflicts_in_file(filepath, markers):
    conflicts = []
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        for lineno, line in enumerate(file, start=1):
            for marker in markers:
                if marker in line:
                    conflicts.append((lineno, marker, line.strip()))
    return conflicts

def scan_directory_for_conflicts(directory, markers, file_extensions=None):
    conflicts_found = {}
    for root, _, files in os.walk(directory):
        for filename in files:
            if file_extensions and not filename.endswith(tuple(file_extensions)):
                continue
            filepath = os.path.join(root, filename)
            conflicts = find_merge_conflicts_in_file(filepath, markers)
            if conflicts:
                conflicts_found[filepath] = conflicts
    return conflicts_found

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Find Git merge conflict symbols in code files.")
    parser.add_argument("path", help="Directory or file to scan")
    parser.add_argument("--ext", nargs='*', help="Limit to specific file extensions, e.g., --ext .py .cpp .js")
    parser.add_argument("--marker-file", required=True, help="Path to file containing merge conflict markers (one per line)")

    args = parser.parse_args()

    conflict_markers = load_conflict_markers(args.marker_file)
    if not conflict_markers:
        print("No conflict markers loaded. Please check the marker file.")
        sys.exit(2)

    conflict_detected = False

    if os.path.isfile(args.path):
        result = find_merge_conflicts_in_file(args.path, conflict_markers)
        if result:
            conflict_detected = True
            print(f"\nMerge conflicts found in: {args.path}")
            for line in result:
                print(f"  Line {line[0]}: {line[1]} -> {line[2]}")
    else:
        result = scan_directory_for_conflicts(args.path, conflict_markers, args.ext)
        if result:
            conflict_detected = True
            for file, conflicts in result.items():
                print(f"\nMerge conflicts found in: {file}")
                for line in conflicts:
                    print(f"  Line {line[0]}: {line[1]} -> {line[2]}")

    if conflict_detected:
        print("\n❌ Merge conflict markers found.")
        sys.exit(1)
    else:
        print("✅ No merge conflicts found.")
        sys.exit(0)
