# Script description

## format_fix.sh

 - TODO

## check_suspect_words.py

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