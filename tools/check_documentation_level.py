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
SUPPORTED_EXTENSIONS = (".h", ".hpp", ".hh", ".hxx", ".c", ".cc", ".cpp", ".cxx")


class DocumentationChecker:

    def __init__(self, source_file):
        self.__lines = []
        self.__all_entities = 0
        self.__commented_entities = 0
        self.__file_errors = []
        self.__source_file = source_file

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
                    self.__lines = []
                    continue

                if "enum " in line:
                    self.__all_entities += 1
                    if any("///" in l and "\\brief" in l for l in self.__lines):
                        self.__commented_entities += 1
                    else:
                        expected = "/// \\brief [enum description]/n (Maybe use enum class instead)"
                        self.add_error(expected)
                    self.__lines = []

                elif "union " in line:
                    self.__all_entities += 1
                    if any("///" in l and "\\brief" in l for l in self.__lines):
                        self.__commented_entities += 1
                    else:
                        expected = "/// \\brief [union description]/n (Unions shouldn't be used at all))"
                        self.add_error(expected)
                    self.__lines = []

                elif line.startswith("const") and ("(" not in line.split("=")[0] or "(" not in line.split("{")[0]):
                    self.__all_entities += 1
                    if any("///" in l for l in self.__lines):
                        self.__commented_entities += 1
                    else:
                        expected = "/// [const description]"
                        self.add_error(expected)
                    self.__lines = []

                elif "(" in line:
                    self.check_one_function(line, f)
                    self.__lines = []
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

        if any("///" in l and "\\brief" in l for l in self.__lines):
            self.__commented_entities += 1
        else:
            expected = "/// \\brief [class/struct description]"
            self.add_error(expected)
        self.__lines = []

        # Looping through class fields looking for functions
        while "{" not in line:
            line = f.readline()
        if "}" not in line:
            curly_brackets = 1
            while curly_brackets != 0:
                line = self.get_next_line(f)

                if "class " in line or "struct " in line:
                    self.check_one_class(line, f)
                    self.__lines = []
                    continue

                if "(" in line:
                    self.check_one_function(line, f, class_name)
                    self.__lines = []
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
                self.__all_entities += 1
                if any("///" in l and "\\brief" in l for l in self.__lines):
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
                    commented_params = sum("\\param" in l for l in self.__lines)
                    self.__commented_entities += commented_params
                    if commented_params != len(function_params):
                        for i in range(len(function_params)):
                            expected += "/// \\param [parameter description]\n\n"

                if function_desc[0].count(" ") > 0 and "void " not in function_desc[0]:
                    self.__all_entities += 1
                    if any("///" in l and "\\return" in l for l in self.__lines):
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

            # Deleting quoted text.
            line = re.sub("[\"].*[\"]", "", line)

            if any(line.startswith(word) for word in WORDS_TO_SKIP):
                self.__lines = []
                line = f.readline()
                continue

            if line.startswith("template"):
                triangle_brackets = line.count("<") - line.count(">")
                while triangle_brackets != 0:
                    line = f.readline()
                    triangle_brackets += line.count("<") - line.count(">")
                line = f.readline()    

            self.__lines.append(line)
            if "//" in line:
                line = f.readline()
                continue

            if not line:
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


def documentation_check(dir_to_check):
    # Checking documentation level for test code and common code. If documentation level is less than 70% - test is failed, otherwise - passed.
    # Results are returned in two dictionaries: with errors and with extended summary (pass/fail).
    root_dir = Path(dir_to_check).expanduser().resolve()
    if not root_dir.exists() or not root_dir.is_dir():
        raise ValueError(f"Directory does not exist or is not a directory: {dir_to_check}")

    files_to_check = get_files_recursive(root_dir, SUPPORTED_EXTENSIONS)
    results = {'test_code': {}, 'common_code': {}}
    extended_results = {'test_code': {}, 'common_code': {}}

    for source_file in files_to_check:
        if source_file.name.endswith("-inl.h"):
            continue

        errors, percent = check_one_file(str(source_file))
        relative_path = source_file.relative_to(root_dir).as_posix()
        category = 'test_code' if 'test' in relative_path.lower() else 'common_code'

        if errors:
            results[category][relative_path] = errors
            extended_results[category][relative_path] = "Fail" if percent < 0.7 else "Pass"
        else:
            extended_results[category][relative_path] = "Pass"

    return results, extended_results

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Check documentation level in source files.")
    parser.add_argument("--dir", required=True, help="Path to source directory")
    args = parser.parse_args()

    results, extended_results = documentation_check(args.dir)

    print("\nDocumentation level check results:")
    for category in results:
        print(f"\nCategory: {category}")
        for file, errors in results[category].items():
            if errors:
                print(f"[FAIL]  {file}")
                for error in errors:
                    print(error)
            else:
                print(f"[PASS]  {file}")

    print("\nExtended summary:")
    for category in extended_results:
        print(f"\nCategory: {category}")
        for file, status in extended_results[category].items():
            print(f"{status}  {file}")
