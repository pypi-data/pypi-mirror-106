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

The argument of the `search` function is the path passed as a string.
#### For Windows
Also, the directory separator should be written in the form `\\`, so as not to form control characters (\n, \t, \r, etc.). Examples:
```
search("C:\\Users")
search("D:\\Downloads\\test.txt")
search("D:\\Git\\cmd")
```
#### Linux
The directory separator should be used `/`. Examples:
```
search("/home/artem/desktop/")
search("/home/artem/tmp/file1")
search("/home/artem/desktop/tmp/")
```
#### Mac OS
The directory separator should be used `/`. Examples:
```
search("/Library/Desktop Pictures")
search("/Library/Desktop Pictures/pictures1.jpg")
search("/Library/Desktop Pictures/gallery")
```
## Code
```
import os
import sys


def search(path):

    base = sys.platform
    sep = "\\"

    if base == "darwin" or "linux":
        sep = "/"

    if os.path.isdir(path):
        try:
            for i in os.listdir(path):
                if os.path.isdir(path + sep + i):
                    search(path + sep + i)
                else:
                    print("\n", path + sep + i)
        except PermissionError:
            print("\n""Отказано в доступе - " + path)
    else:
        if os.path.isfile(path):
            print(path)
        else:
            print("Неверно указан путь!")
```