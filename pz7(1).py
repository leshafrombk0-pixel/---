#Дана строка. Вывести строку, содержащую те же символы, но расположенные в
#обратном порядке.

from functools import reduce
 
reverse_str = lambda s: reduce(lambda acc, c: c + acc, s, "")
 
s = input("Введите строку: ")
print("Обратная строка:", reverse_str(s))
