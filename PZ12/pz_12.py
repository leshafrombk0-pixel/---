#В матрице элементы третьей строки заменить элементами из одномерного
динамического массива соответствующей размерности.
#2. В матрице найти среднее арифметическое положительных элементов

matrix = [
    [12, -5, 3, 8],
    [-2, 10, -7, 4],
    [99, 99, 99, 99],  
    [6, -1, 15, -9],
]

new_row = [5, -3, 8, 14]

print("--- Исходная матрица ---")
for row in matrix:
    print(row)
print(f"\nМассив для замены: {new_row}")

matrix[2] = new_row


for row in matrix:
    for element in row:
        if element > 0:
            positive_elements.append(element)

if positive_elements:
    avg_positive = sum(positive_elements) / len(positive_elements)
else:
    avg_positive = 0  

print("\n========== РЕЗУЛЬТАТЫ ==========")
print("Матрица после замены третьей строки:")
for row in matrix:
    print(row)

print(f"\nНайденные положительные элементы: {positive_elements}")
print(f"Среднее арифметическое положительных элементов: {avg_positive:.2f}")
