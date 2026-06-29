#Дан словарь с произвольным количеством элементов. Выяснить имеется ли в нем
#элемент с ключом «фрукт = яблоко» и если он отсутствует, то добавить его в словарь.
#Вывести на экран первоначальный словарь и измененный

from functools import reduce

sample_dict = {'овощ': 'морковь', 'ягода': 'клубника'}

has_key     = lambda d, k: reduce(lambda acc, x: acc or x == k, d.keys(), False)
add_if_miss = lambda d, k, v: d if has_key(d, k) else {**d, k: v}

print("Первоначальный словарь:", sample_dict)
result = add_if_miss(sample_dict, 'фрукт', 'яблоко')
print("Изменённый словарь:    ", result)
