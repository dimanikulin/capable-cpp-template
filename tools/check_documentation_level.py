#!/usr/bin/env python3
# Copyright {YEAR} YOUR COMPANY NAME.
# All Rights Reserved. The information contained herein is confidential
# property of YOUR COMPANY NAME. The use, copying, transfer or disclosure of such
# information is prohibited except by written agreement with YOUR COMPANY NAME.

import re
from pathlib import Path

# Separator for documentation file.
SEPARATOR_LENGTH = 40
# Skipping line if it starts with:
WORDS_TO_SKIP = ["#", "using ", "typedef "]
SUPPORTED_EXTENSIONS = (".h", ".hpp", ".hh", ".hxx")
DEFAULT_MIN_DOC_LEVEL = 0.7


class DocumentationChecker:

    def __init__(self, source_file):
        self.__lines = []
        self.__all_entities = 0
        self.__commented_entities = 0
        self.__file_errors = []
        self.__source_file = source_file
        self.__inside_block_comment = False
        self.__inside_doxygen_block_comment = False
        self.__has_doxygen_block_doc = False

    def clear_doc_context(self):
        self.__lines = []
        self.__has_doxygen_block_doc = False

    def has_brief_doc(self):
        """Check if \\brief tag exists in documentation lines."""
        return self.__has_doxygen_block_doc or any("\\brief" in l or "@brief" in l for l in self.__lines)

    def has_param_doc(self):
        """Count \\param tags in documentation lines."""
        return sum("\\param" in l or "@param" in l for l in self.__lines)

    def has_return_doc(self):
        """Check if \\return tag exists in documentation lines."""
        return any("\\return" in l or "@return" in l for l in self.__lines)

    def has_any_doc(self):
        """Check if any documentation tags exist in lines."""
        return self.__has_doxygen_block_doc or any(
            "///" in l
            or "\\brief" in l
            or "@brief" in l
            or "\\param" in l
            or "@param" in l
            or "\\return" in l
            or "@return" in l
            for l in self.__lines
        )

    def normalize_block_comment_text(self, text):
        """Extract comment content from a C/C++ block comment line."""
        text = text.strip()
        if text.startswith("/*"):
            text = text[2:]
        if text.endswith("*/"):
            text = text[:-2]
        text = text.lstrip("*!").lstrip()
        return text

    def strip_block_comments(self, line):
        """Remove C/C++ block comments while keeping comment text for doxygen tag detection."""
        cleaned = ""
        current = line
        while current:
            if self.__inside_block_comment:
                end = current.find("*/")
                if end == -1:
                    comment_text = self.normalize_block_comment_text(current)
                    if self.__inside_doxygen_block_comment and comment_text:
                        self.__has_doxygen_block_doc = True
                        self.__lines.append(comment_text)
                    return cleaned
                comment_text = self.normalize_block_comment_text(current[: end + 2])
                if self.__inside_doxygen_block_comment and comment_text:
                    self.__has_doxygen_block_doc = True
                    self.__lines.append(comment_text)
                current = current[end + 2 :]
                self.__inside_block_comment = False
                self.__inside_doxygen_block_comment = False
                continue

            start = current.find("/*")
            if start == -1:
                cleaned += current
                break

            cleaned += current[:start]
            is_doxygen_comment = current.startswith(("/**", "/*!"), start)
            end = current.find("*/", start + 2)
            if end == -1:
                comment_text = self.normalize_block_comment_text(current[start:])
                if is_doxygen_comment and comment_text:
                    self.__has_doxygen_block_doc = True
                    self.__lines.append(comment_text)
                self.__inside_block_comment = True
                self.__inside_doxygen_block_comment = is_doxygen_comment
                break

            comment_text = self.normalize_block_comment_text(current[start : end + 2])
            if is_doxygen_comment and comment_text:
                self.__has_doxygen_block_doc = True
                self.__lines.append(comment_text)
            current = current[end + 2 :]

        return cleaned

    def check_file(self):
        """
        Checks how many doxygen lines are supposed to be in file, and how many there are
        :return: errors list with expected and actual results, documentation level percentage
        """
        with open(self.__source_file, "r", encoding='utf-8') as f:
            # Looping through all lines in file. Breaking if line was not found
            while True:
                line = self.get_next_line(f)
                if not line:
                    break

                if "class " in line or "struct " in line:
                    self.check_one_class(line, f)
                    self.clear_doc_context()
                    continue

                if "enum " in line:
                    self.__all_entities += 1
                    if self.has_brief_doc():
                        self.__commented_entities += 1
                    else:
                        expected = "/// \\brief [enum description]\n (Maybe use enum class instead)"
                        self.add_error(expected)
                    self.clear_doc_context()

                elif "union " in line:
                    self.__all_entities += 1
                    if self.has_brief_doc():
                        self.__commented_entities += 1
                    else:
                        expected = "/// \\brief [union description]\n (Unions shouldn't be used at all))"
                        self.add_error(expected)
                    self.clear_doc_context()

                elif line.startswith("const") and ("(" not in line.split("=")[0] or "(" not in line.split("{")[0]):
                    self.__all_entities += 1
                    if self.has_any_doc():
                        self.__commented_entities += 1
                    else:
                        expected = "/// [const description]"
                        self.add_error(expected)
                    self.clear_doc_context()

                elif "(" in line:
                    self.check_one_function(line, f)
                    self.clear_doc_context()
                    continue

                if "{" in line and "}" not in line:
                    curly_brackets = 1
                    while curly_brackets != 0:
                        line = f.readline()
                        if "{" in line:
                            curly_brackets += 1
                        if "}" in line:
                            curly_brackets -= 1

            if self.__all_entities == 0:
                percent = 1
            else:
                percent = self.__commented_entities / self.__all_entities

            file_name = Path(self.__source_file).as_posix()
            if percent < 0.7:
                print(f"documentation check for file {file_name} failed")
            else:
                print(f"documentation check for file {file_name} is OK")
        return self.__file_errors, percent

    def check_one_class(self, line, f):
        if ";" in line:
            return
        self.__all_entities += 1

        class_name = line.split("class ")
        if len(class_name) == 1:
            class_name = line.split("struct ")
        class_name = class_name[1]
        class_name = re.sub('[{:}\n]', ' ', class_name)
        class_name = class_name.split(" ")[0]

        if self.has_brief_doc():
            self.__commented_entities += 1
        else:
            expected = "/// \\brief [class/struct description]"
            self.add_error(expected)
        self.clear_doc_context()

        # Looping through class fields looking for functions
        while "{" not in line:
            line = f.readline()
        if "}" not in line:
            curly_brackets = 1
            while curly_brackets != 0:
                line = self.get_next_line(f)

                if "class " in line or "struct " in line:
                    self.check_one_class(line, f)
                    self.clear_doc_context()
                    continue

                if "(" in line:
                    self.check_one_function(line, f, class_name)
                    self.clear_doc_context()
                    continue

                if "{" in line:
                    curly_brackets += 1
                if "}" in line:
                    curly_brackets -= 1

    def check_one_function(self, line, f, class_name=""):

        function_desc = line.split("(", 1)
        function_desc[0] = function_desc[0].strip()

        # Skipping lambdas
        if "=" not in function_desc[0] and re.search(r'[^\W\d]', function_desc[0]):
            # Skipping function call but not a declaration
            if function_desc[0].count(" ") != 0 or (not class_name or class_name not in function_desc[0]):
                expected = ""
                has_function_doc = self.has_brief_doc()
                self.__all_entities += 1
                if has_function_doc:
                    self.__commented_entities += 1
                else:
                    expected = "/// \\brief [function description]\n\n"

                function_params = function_desc[1]
                round_brackets = 1 + function_params.count("(") - function_params.count(")")
                while round_brackets != 0:
                    function_params += f.readline()
                    round_brackets = 1  + function_params.count("(") - function_params.count(")")
                function_params = function_params.rsplit(")", 1)[0]
                if not (function_params.strip() == ""):
                    function_params = function_params.split(",")
                    self.__all_entities += len(function_params)
                    commented_params = self.has_param_doc()
                    if commented_params:
                        self.__commented_entities += commented_params
                    elif has_function_doc:
                        self.__commented_entities += len(function_params)
                    if not has_function_doc and commented_params != len(function_params):
                        for i in range(len(function_params)):
                            expected += "/// \\param [parameter description]\n\n"

                if function_desc[0].count(" ") > 0 and "void " not in function_desc[0]:
                    self.__all_entities += 1
                    if self.has_return_doc():
                        self.__commented_entities += 1
                    elif has_function_doc:
                        self.__commented_entities += 1
                    else:
                        expected += "/// \\return [return description]"

                if expected:
                    self.add_error(expected)

            while ";" not in line and "{" not in line:
                line = f.readline()

            if "{" in line and "}" not in line:
                curly_brackets = 1
                while curly_brackets != 0:
                    line = f.readline()
                    if "{" in line:
                        curly_brackets += 1
                    if "}" in line:
                        curly_brackets -= 1

    def get_next_line(self, f):
        line = f.readline()
        while line:
            line = line.strip()

            # Deleting quoted text.
            line = re.sub("[\"]*[\"]", "", line)
            line = self.strip_block_comments(line).strip()

            if "namespace " in line:
                while "{" not in line and ";" not in line:
                    line = f.readline()
                line = f.readline()
                continue

            line = line.replace("static ", '')
            line = line.replace("extern ", '')
            line = line.replace("virtual ", '')
            line = line.replace("volatile ", '')
            line = line.replace("register ", '')
            line = line.strip()

            if any(line.startswith(word) for word in WORDS_TO_SKIP):
                self.clear_doc_context()
                line = f.readline()
                continue

            if line.startswith("template"):
                triangle_brackets = line.count("<") - line.count(">")
                while triangle_brackets != 0:
                    line = f.readline()
                    triangle_brackets += line.count("<") - line.count(">")
                line = f.readline()

            if not line:
                line = f.readline()
                continue

            self.__lines.append(line)
            if "//" in line:
                line = f.readline()
                continue

            break
        return line

    def add_error(self, expected):
        self.__file_errors.append('==' * SEPARATOR_LENGTH)
        self.__file_errors.append('FILE: {}'.format(self.__source_file))
        self.__file_errors.append('==' * SEPARATOR_LENGTH)

        self.__file_errors.append('Valid doxygen line not found\n')
        self.__file_errors.append('Expected: "{}"\n'.format(expected))

        self.__file_errors.append('Actual: ')
        self.__file_errors.append('"""')
        for line in self.__lines[-3:]:
            self.__file_errors.append(line)
        self.__file_errors.append('...')
        self.__file_errors.append('"""')


def check_one_file(source_file):
    d = DocumentationChecker(source_file)
    return d.check_file()


def get_files_recursive(directory, extensions):
    directory = Path(directory)
    files = []
    for extension in extensions:
        files.extend(directory.rglob(f"*{extension}"))
    return sorted(set(files))


def documentation_check(dir_to_check, min_doc_level=DEFAULT_MIN_DOC_LEVEL):
    # Checking documentation level for all code files. If documentation level is less than 70% - test is failed, otherwise - passed.
    # Results are returned in two dictionaries: one with errors and one with extended summary (pass/fail).
    root_dir = Path(dir_to_check).expanduser().resolve()
    if not root_dir.exists() or not root_dir.is_dir():
        raise ValueError(f"Directory does not exist or is not a directory: {dir_to_check}")

    files_to_check = get_files_recursive(root_dir, SUPPORTED_EXTENSIONS)
    results = {}
    extended_results = {}

    for source_file in files_to_check:
        if source_file.name.endswith("-inl.h"):
            continue

        errors, percent = check_one_file(str(source_file))
        relative_path = source_file.relative_to(root_dir).as_posix()

        if errors:
            results[relative_path] = errors
            extended_results[relative_path] = "Fail" if percent < min_doc_level else "Pass"
        else:
            extended_results[relative_path] = "Pass"

    return results, extended_results

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Check documentation level in source files.")
    parser.add_argument("--dir", required=True, help="Path to source directory")
    parser.add_argument(
        "--min-doc-level",
        type=float,
        default=DEFAULT_MIN_DOC_LEVEL,
        help="Minimum documentation level threshold in range [0.0, 1.0]",
    )
    args = parser.parse_args()

    if not 0.0 <= args.min_doc_level <= 1.0:
        raise ValueError("--min-doc-level must be between 0.0 and 1.0")

    results, extended_results = documentation_check(args.dir, min_doc_level=args.min_doc_level)

    print("\nDocumentation level check results:")
    for file, errors in results.items():
        if errors:
            print(f"[FAIL]  {file}")
            for error in errors:
                print(error)
        else:
            print(f"[PASS]  {file}")

    print("\nExtended summary:")
    for file, status in extended_results.items():
        print(f"{status}  {file}")
