from functools import reduce

get_last_dir = lambda path: (
    parts[-2] if (parts := list(filter(None, path.replace("\\", "/").split("/"))))[:-1]
    else "\\"
)

path = input("Введите полный путь к файлу: ")
print("Последний каталог:", get_last_dir(path))
