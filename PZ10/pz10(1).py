#10.1 - Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Исходные данные:
#Количество элементов:
#Элементы в обратном порядке:
#Сумма элементов последней половины:

from functools import reduce

# --- Константы ---
INPUT_FILE   = "data_10_1.txt"
OUTPUT_FILE  = "data_10_2.txt"
INITIAL_DATA = "-10 15 20 -5 30 -40 50 60"

# --- Чистые функции ---
write_file     = lambda path, text: open(path, "w", encoding="utf-8").write(text)
read_file      = lambda path: open(path, "r", encoding="utf-8").read()

parse_numbers  = lambda text: list(map(int, text.split()))
count_elements = lambda lst: reduce(lambda acc, _: acc + 1, lst, 0)
reverse_list   = lambda lst: list(reversed(lst))
to_str_list    = lambda lst: list(map(str, lst))
join_spaces    = lambda lst: reduce(lambda a, b: a + " " + b, lst)

half_index     = lambda lst: count_elements(lst) // 2
second_half    = lambda lst: lst[half_index(lst):]
second_half_sum= lambda lst: reduce(lambda acc, x: acc + x, second_half(lst), 0)

format_result  = lambda raw, nums: (
    f"Исходные данные: {raw}\n"
    f"Количество элементов: {count_elements(nums)}\n"
    f"Элементы в обратном порядке: {join_spaces(to_str_list(reverse_list(nums)))}\n"
    f"Сумма элементов последней половины: {second_half_sum(nums)}\n"
)

# --- Точка входа ---
if __name__ == "__main__":
    # 1. Создаём исходный файл
    write_file(INPUT_FILE, INITIAL_DATA)

    # 2. Читаем и парсим
    raw     = read_file(INPUT_FILE)
    numbers = parse_numbers(raw)

    # 3. Формируем и записываем результат
    result  = format_result(raw, numbers)
    write_file(OUTPUT_FILE, result)

    # 4. Выводим
    print("--- Задача выполнена. Содержимое нового файла: ---")
    print(read_file(OUTPUT_FILE))
#10.1 - Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Исходные данные:
#Количество элементов:
#Элементы в обратном порядке:
#Сумма элементов последней половины:

# 1. Создаем исходный файл с числами (Вариант 10)
initial_numbers = "-10 15 20 -5 30 -40 50 60"
with open("data_10_1.txt", "w", encoding="utf-8") as f1:
    f1.write(initial_numbers)

# 2. Читаем числа и переводим их в список целых чисел
with open("data_10_1.txt", "r", encoding="utf-8") as f1:
    content = f1.read().split()

numbers = [int(x) for x in content]

# 3. Выполняем обработку по ТЗ Варианта 10
count_elements = len(numbers)  # Количество элементов
reversed_elements = " ".join(
    [str(x) for x in reversed(numbers)]
)  # В обратном порядке

# Находим сумму элементов последней половины
half_index = len(numbers) // 2
second_half_sum = sum(numbers[half_index:])

# 4. Записываем результат в новый файл
with open("data_10_2.txt", "w", encoding="utf-8") as f2:
    f2.write(f"Исходные данные: {initial_numbers}\n")
    f2.write(f"Количество элементов: {count_elements}\n")
    f2.write(f"Элементы в обратном порядке: {reversed_elements}\n")
    f2.write(f"Сумма элементов последней половины: {second_half_sum}\n")

# Выводим в консоль для проверки в Colab
print("--- Задача 1 выполнена. Содержимое нового файла: ---")
with open("data_10_2.txt", "r", encoding="utf-8") as f2:
    print(f2.read())
