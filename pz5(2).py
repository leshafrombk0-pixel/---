#Описать функцию Minmax(X, Y), записывающую в переменную X минимальное из
#значений X и Y, а в переменную Y — максимальное из этих значений (X и Y —
#вещественные параметры, являющиеся одновременно входными и выходными).
#Используя четыре вызова этой функции, найти минимальное и максимальное из
#данных чисел A, B, C, D


from functools import reduce

# --- Чистые функции ---
minmax = lambda x, y: (min(x, y), max(x, y))

# 4 вызова minmax для нахождения минимума и максимума из A, B, C, D
def find_minmax(a, b, c, d):
    a, b = minmax(a, b)   # вызов 1: a=min(a,b), b=max(a,b)
    c, d = minmax(c, d)   # вызов 2: c=min(c,d), d=max(c,d)
    a, c = minmax(a, c)   # вызов 3: a=общий минимум
    b, d = minmax(b, d)   # вызов 4: d=общий максимум
    return a, d

# --- Точка входа ---
get_float = lambda prompt: float(input(prompt))

A = get_float("Введите A: ")
B = get_float("Введите B: ")
C = get_float("Введите C: ")
D = get_float("Введите D: ")

minimum, maximum = find_minmax(A, B, C, D)

print(f"Минимальное: {minimum}")
print(f"Максимальное: {maximum}")
