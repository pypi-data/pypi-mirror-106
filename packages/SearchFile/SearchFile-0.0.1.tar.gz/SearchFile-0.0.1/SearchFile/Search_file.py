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

