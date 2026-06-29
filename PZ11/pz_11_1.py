from functools import reduce

# --- Входные данные (заданы вручную) ---
def get_numbers():
    return [-3, 7, -1, 4, -8, 2, 0, -5, 9, 6]

# --- Чистые функции обработки ---
is_negative = lambda x: x < 0
is_even     = lambda x: x % 2 == 0

def max_negative(numbers):
    negatives = list(filter(is_negative, numbers))
    return reduce(lambda a, b: a if a > b else b, negatives) if negatives else "Отрицательных чисел нет"

def even_numbers(numbers):
    return list(filter(is_even, numbers))

def even_sum(numbers):
    evens = even_numbers(numbers)
    return reduce(lambda a, b: a + b, evens, 0)

# --- Функция вывода ---
def print_results(numbers):
    results = {
        "Исходная последовательность": numbers,
        "1. Максимальный среди отрицательных": max_negative(numbers),
        "2. Элементы, кратные двум": even_numbers(numbers),
        "3. Их сумма": even_sum(numbers),
    }
    print("\n========== РЕЗУЛЬТАТЫ ==========")
    list(map(lambda item: print(f"{item[0]}: {item[1]}"), results.items()))

# --- Точка входа ---
if __name__ == "__main__":
    print_results(get_numbers())
