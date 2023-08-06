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
