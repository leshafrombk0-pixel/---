#Проверьте наличие значения 200 в sample_dict = {'a': 100, 'b': 200, 'c': 300}.


from functools import reduce

sample_dict = {'a': 100, 'b': 200, 'c': 300}

has_value = lambda d, v: reduce(lambda acc, x: acc or x == v, d.values(), False)

print("Словарь:", sample_dict)
print("Значение 200 есть:", has_value(sample_dict, 200))
