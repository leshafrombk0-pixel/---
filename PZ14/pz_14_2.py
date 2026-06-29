#Разработать программу с применением пакета tk, взяв в качестве условия одну
#любую задачу из ПЗ №№ 1 – 9.


import tkinter as tk
from tkinter import messagebox

# --- Логика вычислений (Чистые функции) ---
count_segments = lambda a, b: a // b
unused_length = lambda a, b: a % b


# --- Обработчик нажатия на кнопку ---
def calculate():
    try:
        # Получаем данные из полей ввода
        a_val = int(entry_A.get())
        b_val = int(entry_B.get())

        # Валидация входных данных по условию задачи
        if a_val <= 0 or b_val <= 0:
            raise ValueError("Числа должны быть положительными!")
        if a_val <= b_val:
            raise ValueError("Длина A должна быть строго больше B!")

        # Вычисления
        segments = count_segments(a_val, b_val)
        remainder = unused_length(a_val, b_val)

        # Вывод результата в текстовую метку
        label_result.config(
            text=f"Количество отрезков B: {segments}\nНезанятая часть отрезка A: {remainder}",
            fg="green",
        )

    except ValueError as e:
        # Если ввели не числа или нарушили условия A > B > 0
        error_msg = str(e)
        if "invalid literal" in error_msg:
            error_msg = "Пожалуйста, введите целые числа!"
        messagebox.showerror("Ошибка ввода", error_msg)


# --- Создание главного окна ---
root = tk.Tk()
root.title("Размещение отрезков")
root.geometry("360x240")
root.resizable(False, False)

# --- Элементы интерфейса (Виджеты) ---
# Поле ввода для отрезка A
label_A = tk.Label(root, text="Введите длину отрезка A:", font=("Arial", 10))
label_A.pack(pady=(15, 2))
entry_A = tk.Entry(root, font=("Arial", 10), justify="center")
entry_A.pack(pady=2)

# Поле ввода для отрезка B
label_B = tk.Label(root, text="Введите длину отрезка B (B < A):", font=("Arial", 10))
label_B.pack(pady=(10, 2))
entry_B = tk.Entry(root, font=("Arial", 10), justify="center")
entry_B.pack(pady=2)

# Кнопка расчета
btn_calc = tk.Button(
    root,
    text="Рассчитать",
    font=("Arial", 10, "bold"),
    command=calculate,
    bg="#4CAF50",
    fg="white",
)
btn_calc.pack(pady=15)

# Метка для вывода результатов
label_result = tk.Label(root, text="", font=("Arial", 10, "bold"), justify="left")
label_result.pack(pady=5)

# Запуск главного цикла приложения
root.mainloop()
