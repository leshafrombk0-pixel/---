# Дано целое число N (> 0). Найти сумму N^2 + (N+1)^2 + ... + (2N)^2

n = input("Введите целое число N (> 0): ")
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите целое число N (> 0): ")

while n <= 0:
    print("N должно быть больше 0!")
    n = input("Введите целое число N (> 0): ")
    while type(n) != int:
        try:
            n = int(n)
        except ValueError:
            print("Неправильно ввели!")
            n = input("Введите целое число N (> 0): ")

s = 0
i = n
while i <= 2 * n:
    s += i * i
    i += 1

print("Сумма:", s)
