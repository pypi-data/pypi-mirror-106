# SearchFile
#### Table of contents
1. [Installation](#Installation)
2. [Description](#Description)
3. [Using](#Using)
4. [Code](#Code)
## Installation
Installation using a terminal:

```pip install SearchFile```
## Description
This library is designed to search for files by a given path.s the path we pass.
## Using
```import SearchFile```

or

```from SearchFile import search```

The argument of the `search` function is the path passed as a string. Also, the directory separator should be written in the form `\\`, so as not to form control characters (\n, \t, \r, etc.). Examples:
```
search("C:\\Users")
search("D:\\Скачанные файлы\\test.txt")
search("D:\\Git\\cmd")
```
## Code
```
import os


def search(path):
    if os.path.isdir(path):
        try:
            for i in os.listdir(path):
                if os.path.isdir(path + "\\" + i):
                    search(path + "\\" + i)
                else:
                    print("\n", path + "\\" + i)
        except PermissionError:
            print("\n""Отказано в доступе - " + path)
    else:
        if os.path.isfile(path):
            print(path)
        else:
            print("Неверно указан путь!")
```