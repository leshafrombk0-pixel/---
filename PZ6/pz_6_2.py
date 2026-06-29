# Дан список размера N. Найти количество его промежутков монотонности
# (участков, на которых элементы строго возрастают или строго убывают).
from functools import reduce
n = input("Введите размер списка N: ")
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите размер списка N: ")

while n <= 0:
    print("N должно быть больше 0!")
    n = input("Введите размер списка N: ")
    while type(n) != int:
        try:
            n = int(n)
        except ValueError:
            print("Неправильно ввели!")
            n = input("Введите размер списка N: ")

a = []
i = 0
while i < n:
    x = input(f"Введите элемент a[{i}]: ")
    while type(x) != int:
        try:
            x = int(x)
        except ValueError:
            print("Неправильно ввели!")
            x = input(f"Введите элемент a[{i}]: ")
    a.append(x)
    i += 1

print("Список:", a)


if n < 2:
    print("Количество промежутков монотонности:", 0)
else:
    count = 0
    prev_sign = 0

    i = 1
    while i < n:
        d = a[i] - a[i - 1]

        if d > 0:
            sign = 1
        elif d < 0:
            sign = -1
        else:
            sign = 0

        if sign != 0:
            if prev_sign == 0:
                count = 1
                prev_sign = sign
            elif sign != prev_sign:
                count += 1
                prev_sign = sign

        i += 1

    print("Количество промежутков монотонности:", count)
