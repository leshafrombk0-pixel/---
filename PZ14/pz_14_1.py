#Задание 1. В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
#его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
#приближенный к оригиналу (см. таблицу 1)


import tkinter as tk
from tkinter import ttk


def create_contact_form():
    # Создаем главное окно
    root = tk.Tk()
    root.title("Contact Form")

    # Задаем размер окна и серый фон вокруг формы
    root.geometry("600x650")
    root.configure(bg="#2d2d2d")

    # Основная рамка (карточка формы) с текстурным серым цветом
    form_frame = tk.Frame(root, bg="#e0e0e0", bd=1, relief="solid")
    form_frame.place(relx=0.5, rely=0.5, anchor="center", width=450, height=550)

    # Заголовок "Contact Form"
    title_label = tk.Label(
        form_frame,
        text="Contact Form",
        font=("Arial", 24, "bold"),
        bg="#e0e0e0",
        fg="#000000",
    )
    title_label.pack(pady=(30, 5))

    # Подзаголовок "Please fill all entries."
    subtitle_label = tk.Label(
        form_frame,
        text="Please fill all entries.",
        font=("Arial", 11, "bold"),
        bg="#e0e0e0",
        fg="#222222",
    )
    subtitle_label.pack(pady=(0, 10))

    # Тонкая разделительная линия
    separator = tk.Frame(form_frame, height=1, bg="#b5b5b5")
    separator.pack(fill="x", padx=40, pady=(0, 25))

    # Контейнер для полей ввода (чтобы выровнять метки по правому краю)
    fields_frame = tk.Frame(form_frame, bg="#e0e0e0")
    fields_frame.pack(fill="both", expand=True, padx=40)

    # Настройка сеток для выравнивания
    fields_frame.columnconfigure(0, weight=1)  # Колонна для текста (меток)
    fields_frame.columnconfigure(1, weight=3)  # Колонна для полей ввода

    # Стиль для шрифта меток
    label_font = ("Arial", 12)

    # 1. Поле Name
    name_label = tk.Label(
        fields_frame, text="Name :", font=label_font, bg="#e0e0e0", anchor="e"
    )
    name_label.grid(row=0, column=0, sticky="e", padx=(0, 15), pady=10)

    name_entry = tk.Entry(
        fields_frame, font=("Arial", 11), bd=1, relief="solid", bg="white"
    )
    name_entry.grid(row=0, column=1, sticky="ew", ipady=4, pady=10)

    # 2. Поле Email
    email_label = tk.Label(
        fields_frame, text="Email :", font=label_font, bg="#e0e0e0", anchor="e"
    )
    email_label.grid(row=1, column=0, sticky="e", padx=(0, 15), pady=10)

    email_entry = tk.Entry(
        fields_frame, font=("Arial", 11), bd=1, relief="solid", bg="white"
    )
    email_entry.grid(row=1, column=1, sticky="ew", ipady=4, pady=10)

    # 3. Поле Message
    message_label = tk.Label(
        fields_frame,
        text="Message :",
        font=label_font,
        bg="#e0e0e0",
        anchor="e",
    )
    message_label.grid(row=2, column=0, sticky="ne", padx=(0, 15), pady=10)

    # Используем tk.Text для многострочного текста (содержит "уголок" для изменения размера в оригинале)
    message_text = tk.Text(
        fields_frame,
        font=("Arial", 11),
        bd=1,
        relief="solid",
        bg="white",
        height=5,
    )
    message_text.grid(row=2, column=1, sticky="ew", pady=10)

    # 4. Поле Subject (Выпадающий список)
    subject_label = tk.Label(
        fields_frame,
        text="Subject :",
        font=label_font,
        bg="#e0e0e0",
        anchor="e",
    )
    subject_label.grid(row=3, column=0, sticky="e", padx=(0, 15), pady=15)

    # Настройка стиля для ttk.Combobox, чтобы убрать лишние рамки
    style = ttk.Style()
    style.theme_use("clam")
    style.configure(
        "TCombobox",
        fieldbackground="white",
        background="white",
        darkcolor="gray",
        lightcolor="gray",
    )

    subject_combobox = ttk.Combobox(
        fields_frame,
        font=("Arial", 10),
        style="TCombobox",
        values=["Product Inquiry", "Service Support", "Feedback", "Other"],
    )
    subject_combobox.current(0)  # Устанавливаем значение по умолчанию
    subject_combobox.grid(row=3, column=1, sticky="ew", ipady=3, pady=15)

    # Кнопка Send (темно-серая с градиентным эффектом)
    send_button = tk.Button(
        form_frame,
        text="Send",
        font=("Arial", 11, "bold"),
        bg="#5a5a5a",
        fg="white",
        activebackground="#4a4a4a",
        activeforeground="white",
        bd=1,
        relief="raised",
        cursor="hand2",
    )
    send_button.pack(pady=(0, 35), ipadx=25, ipady=5)

    # Запуск главного цикла приложения
    root.mainloop()


if __name__ == "__main__":
    create_contact_form()
