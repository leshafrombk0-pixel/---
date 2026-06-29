# Дано целое число N (> 1). Найти наибольшее целое число K, при котором 3^K < N

n = input("Введите целое число N (> 1): ")
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите целое число N (> 1): ")

while n <= 1:
    print("N должно быть больше 1!")
    n = input("Введите целое число N (> 1): ")
    while type(n) != int:
        try:
            n = int(n)
        except ValueError:
            print("Неправильно ввели!")
            n = input("Введите целое число N (> 1): ")

k = 0
p = 1

while p * 3 < n:
    p *= 3
    k += 1

print("Наибольшее целое K, при котором 3^K < N:", k)
