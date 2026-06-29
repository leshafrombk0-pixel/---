#Даны два целых числа: A, B. Проверить истинность высказывания: «Ровно одно из
#чисел A и B нечетное».

from functools import reduce
 
# ==============================
# Задача 1: Ровно одно нечётное
# ==============================
 
safe_int = lambda prompt: int(input(prompt))
 
A = safe_int("Введите A: ")
B = safe_int("Введите B: ")
 
is_odd        = lambda x: x % 2 != 0
exactly_one   = lambda a, b: is_odd(a) != is_odd(b)  # XOR через !=
 
print("Ровно одно нечётное:", exactly_one(A, B))
