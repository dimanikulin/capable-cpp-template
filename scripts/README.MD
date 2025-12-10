# format_fix.sh

 - It fixes the code formatting according to *.clang-format* format configuration in the root dir.

# format_fix_cmake.sh
- It the CMakeLists.file according to *..cmake-format.yaml* format configuration in the root dir.

# check_suspect_words.py

- Create marker file with suspect words
```bash
echo -e "<<<<<<<\n=======\n>>>>>>>" > markers.txt
```

- Scan all files in current directory
```bash
python check_suspect_words.py . --marker-file markers.txt --ext .py .cpp
```

- Scan only `.py` and `.cpp` files in a src folder
```bash
python check_suspect_words.py ./src --marker-file markers.txt --ext .py .cpp
```
# check_boilerplates.py

It recursively scans the directory for source files (you can define which extensions to include). Then it compares the beginning of each file against the boilerplate template. Finally it print which files pass or fail.

It accepts two parameters:

- src → path to the input source directory
- boilerplate → path to a reference boilerplate template file

```bash
python check_boilerplate.py --src ./my_project --boilerplate ./boilerplate.txt --ext .cpp .h
```
boilerplate.txt = your reference boilerplate (e.g., license header).

It will check the first N lines of each file (where N is the number of lines in the boilerplate).

# check_file_size.py
It 
- Walks the directory recursively.
- For each file → count code lines.
- Compares with the max allowed.

Collects:
- number of files within limit
- number of files exceeding limit

At the end → prints statistics + exit non-zero if any failed.

## Usage
python count_code_lines.py <dir> <max_lines> [comment_symbol] [ext1 ext2 ...]

Check all Python files under src/, max 500 lines allowed:
```bash
python count_code_lines.py src 500 "#" .py
```

Check all C++ files under project/, max 2000 lines allowed:
```bash
python count_code_lines.py project 2000 "//" .cpp .h
```
