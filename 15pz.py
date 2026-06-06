import os
import sqlite3
import tkinter as tk
from datetime import datetime
from tkinter import messagebox, ttk


class IndustryApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Учет промышленных предприятий")
        self.root.geometry("1100x650")
        self.root.configure(bg="#f4f4f4")

        # Имя файла базы данных
        self.db_name = "industry.db"

        # Инициализируем базу данных и интерфейс
        self.init_db()
        self.create_widgets()
        self.refresh_table()

    def init_db(self):
        """Создание таблицы и заполнение 10 начальными позициями (ТЗ)."""
        try:
            # Если базы нет, она создастся, если есть — просто подключится
            db_is_new = not os.path.exists(self.db_name)
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()

            # Создаем таблицу по структуре из ТЗ
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS enterprises (
                    code INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    address TEXT NOT NULL,
                    branches INTEGER NOT NULL,
                    staff INTEGER NOT NULL,
                    equipment_cost REAL NOT NULL,
                    production_volume REAL NOT NULL,
                    reg_date TEXT NOT NULL
                )
            """)
            self.conn.commit()

            # Если база только что создана, заполняем её 10 позициями
            if db_is_new:
                sample_data = [
                    (
                        "Гомсельмаш",
                        "г. Гомель, ул. Шоссейная, 41",
                        5,
                        8500,
                        1250000.0,
                        5000000.0,
                        "2001-05-12",
                    ),
                    (
                        "МТЗ",
                        "г. Минск, ул. Долгобродская, 29",
                        12,
                        15000,
                        3400000.0,
                        9200000.0,
                        "1996-02-20",
                    ),
                    (
                        "МАЗ",
                        "г. Минск, ул. Социалистическая, 2",
                        8,
                        11000,
                        2800000.0,
                        7100000.0,
                        "1998-08-15",
                    ),
                    (
                        "БЕЛАЗ",
                        "г. Жодино, ул. 40 лет Октября, 4",
                        3,
                        9000,
                        4100000.0,
                        11500000.0,
                        "2003-11-01",
                    ),
                    (
                        "Интеграл",
                        "г. Минск, ул. Казинца, 121а",
                        4,
                        4500,
                        1900000.0,
                        3200000.0,
                        "2000-03-14",
                    ),
                    (
                        "Гродно Азот",
                        "г. Гродно, пр-т Космонавтов, 100",
                        2,
                        6800,
                        2500000.0,
                        6400000.0,
                        "1995-07-22",
                    ),
                    (
                        "Белшина",
                        "г. Бобруйск, Минское шоссе",
                        6,
                        7200,
                        1800000.0,
                        4800000.0,
                        "2002-04-18",
                    ),
                    (
                        "Могилевхимволокно",
                        "г. Могилев, ул. Челюскинцев",
                        2,
                        5100,
                        1350000.0,
                        2900000.0,
                        "1999-10-05",
                    ),
                    (
                        "Нафтан",
                        "г. Новополоцк, ул. Промышленная",
                        1,
                        8000,
                        5200000.0,
                        14000000.0,
                        "1994-01-30",
                    ),
                    (
                        "БМЗ",
                        "г. Жлобин, ул. Промышленная, 37",
                        7,
                        10500,
                        3900000.0,
                        8800000.0,
                        "2005-09-09",
                    ),
                ]
                self.cursor.executemany(
                    """
                    INSERT INTO enterprises (name, address, branches, staff, equipment_cost, production_volume, reg_date)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                    sample_data,
                )
                self.conn.commit()
        except sqlite3.Error as e:
            messagebox.showerror(
                "Ошибка БД", f"Не удалось инициализировать БД: {e}"
            )

    def create_widgets(self):
        """Создание элементов графического интерфейса."""
        # --- Левая панель: Ввод и редактирование данных ---
        input_frame = tk.LabelFrame(
            self.root, text="Данные предприятия", bg="#f4f4f4", font=("Arial", 10, "bold")
        )
        input_frame.place(x=15, y=15, width=320, height=360)

        # Текстовые метки и поля ввода
        labels = [
            "Код (только для ред.):",
            "Наименование:",
            "Физический адрес:",
            "Кол-во филиалов:",
            "Численность персонала:",
            "Стоимость оборуд. (руб):",
            "Объем продукции (руб):",
            "Дата рег. (ГГГГ-ММ-ДД):",
        ]
        self.entries = {}

        for i, text in enumerate(labels):
            lbl = tk.Label(input_frame, text=text, bg="#f4f4f4", anchor="w")
            lbl.grid(row=i, column=0, sticky="ew", padx=10, pady=3)

            entry = tk.Entry(input_frame)
            entry.grid(row=i, column=1, sticky="ew", padx=10, pady=3)

            # Сохраняем ссылки на поля, чтобы брать из них текст
            key = [
                "code",
                "name",
                "address",
                "branches",
                "staff",
                "eq_cost",
                "volume",
                "date",
            ][i]
            self.entries[key] = entry

        # Поле кода делаем изначально заблокированным для ручного ввода при добавлении
        self.entries["code"].configure(
            bg="#e0e0e0"
        )  # Код генерируется БД автоматически

        # Кнопки под полями ввода
        btn_add = tk.Button(
            input_frame,
            text="Добавить новую запись",
            bg="#4CAF50",
            fg="white",
            command=self.add_record,
        )
        btn_add.grid(row=8, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

        # --- Правая панель: Таблица для отображения БД ---
        table_frame = tk.Frame(self.root)
        table_frame.place(x=350, y=15, width=730, height=360)

        columns = ("code", "name", "address", "branches", "staff", "cost", "vol", "date")
        self.tree = ttk.Treeview(
            table_frame, columns=columns, show="headings", selectmode="browse"
        )

        # Заголовки колонок
        self.tree.heading("code", text="Код")
        self.tree.heading("name", text="Название")
        self.tree.heading("address", text="Адрес")
        self.tree.heading("branches", text="Филиалы")
        self.tree.heading("staff", text="Персонал")
        self.tree.heading("cost", text="Стоим. обор.")
        self.tree.heading("vol", text="Объем прод.")
        self.tree.heading("date", text="Дата рег.")

        # Ширина колонок
        self.tree.column("code", width=40, anchor="center")
        self.tree.column("name", width=100)
        self.tree.column("address", width=120)
        self.tree.column("branches", width=60, anchor="center")
        self.tree.column("staff", width=70, anchor="center")
        self.tree.column("cost", width=90)
        self.tree.column("vol", width=90)
        self.tree.column("date", width=80, anchor="center")

        # Прокрутка для таблицы
        scrollbar = ttk.Scrollbar(
            table_frame, orient="vertical", command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # При клике на строку таблицы данные переносятся в поля ввода
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        # --- Нижняя панель: Управление (Поиск, Редактирование, Удаление) ---
        control_frame = tk.LabelFrame(
            self.root, text="Операции (по 3 SQL-запроса на действие)", bg="#f4f4f4", font=("Arial", 10, "bold")
        )
        control_frame.place(x=15, y=390, width=1065, height=230)

        # Блок редактирования (3 разных SQL запроса в зависимости от условий)
        edit_lbl = tk.Label(
            control_frame,
            text="РЕДАКТИРОВАНИЕ (выберите строку в таблице, измените поля слева):",
            bg="#f4f4f4",
            font=("Arial", 9, "bold"),
        )
        edit_lbl.grid(row=0, column=0, columnspan=3, sticky="w", padx=10, pady=(5, 2))

        tk.Button(
            control_frame,
            text="Запрос 1: Обновить ВСЕ поля предприятия",
            bg="#2196F3",
            fg="white",
            command=lambda: self.edit_record(1),
        ).grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        tk.Button(
            control_frame,
            text="Запрос 2: Сбросить филиалы в 0 (если закрылись)",
            bg="#2196F3",
            fg="white",
            command=lambda: self.edit_record(2),
        ).grid(row=1, column=1, padx=5, pady=5, sticky="ew")
