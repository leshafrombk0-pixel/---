#Туристические агентства предлагают следующие туры. Вояж – Мексика,Канада,Израиль,
#Италия,США. РейнаТур – Англия,Япония,Канада,ЮАР. Радуга – США,Испания,Швеция,
#Австралия. Определить:
#1. в каких турагенствах можно приобрести туры в Японию.
#2. в каких турагенствах нельзя приобрести туры в ЮАР.
#3. полный список всех туров.



from functools import reduce

agencies = {
    'Вояж':    {'Мексика', 'Канада', 'Израиль', 'Италия', 'США'},
    'РейнаТур':{'Англия', 'Япония', 'Канада', 'ЮАР'},
    'Радуга':  {'США', 'Испания', 'Швеция', 'Австралия'},
}

has_country    = lambda country: lambda name, tours: country in tours
hasnt_country  = lambda country: lambda name, tours: country not in tours

filter_agencies = lambda pred: list(map(
    lambda item: item[0],
    filter(lambda item: pred(*item), agencies.items())
))

all_tours = reduce(lambda acc, tours: acc | tours, agencies.values(), set())

print("1. Туры в Японию:      ", filter_agencies(has_country('Япония')))
print("2. Нет туров в ЮАР:   ", filter_agencies(hasnt_country('ЮАР')))
print("3. Все туры:           ", all_tours)
