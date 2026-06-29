#Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из
#результата вновь вычли сумму его цифр и т. д. Через сколько таких действий
#получится нуль?

from functools import reduce

# --- Чистые функции ---
digit_sum  = lambda n: reduce(lambda acc, d: acc + int(d), str(n), 0)
subtract   = lambda n: n - digit_sum(n)

def count_steps(n, steps=0):
    return steps if n == 0 else count_steps(subtract(n), steps + 1)

# --- Точка входа ---
n = int(input("Введите число: "))
print(f"Количество шагов до нуля: {count_steps(n)}")
