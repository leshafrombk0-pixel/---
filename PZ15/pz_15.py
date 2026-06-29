#Приложение ПРОМЫШЛЕННОСТЬ для автоматизированного учета информации
#о промышленных предприятиях республики. БД содержит таблицу Предприятия,
#имеющую следующую структуру записи: Код предприятия, Наименование предприятия,
#Физический адрес, Филиалы (количество филиалов), Общая числ. персонала, Общая стоим.
#оборудования, Объем выпускаемой продукции, Дата регистрации

import os
import sqlite3
import tkinter as tk
from datetime import datetime
from tkinter import messagebox, ttk


class IndustryApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Учет промышленных предприятий")
        self.root.geometry("1150x650")
        self.root.configure(bg="#f4f4f4")

        self.db_name = "industry.db"

        self.init_db()
        self.create_widgets()
        self.refresh_table()

    def init_db(self):
        """Создание таблицы и заполнение 10 начальными позициями (ТЗ)."""
        try:
            db_is_new = not os.path.exists(self.db_name)
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()

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
            print(f"Ошибка БД: {e}")

    def create_widgets(self):
        """Создание элементов графического интерфейса."""
        input_frame = tk.LabelFrame(
            self.root,
            text="Данные предприятия",
            bg="#f4f4f4",
            font=("Arial", 10, "bold"),
        )
        input_frame.place(x=15, y=15, width=340, height=360)

        labels = [
            "Код (только ред.):",
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
            lbl.grid(row=i, column=0, sticky="ew", padx=5, pady=3)

            entry = tk.Entry(input_frame)
            entry.grid(row=i, column=1, sticky="ew", padx=5, pady=3)

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

        self.entries["code"].configure(bg="#e0e0e0")

        btn_add = tk.Button(
            input_frame,
            text="Добавить новую запись",
            bg="#4CAF50",
            fg="white",
            command=self.add_record,
        )
        btn_add.grid(
            row=8, column=0, columnspan=2, sticky="ew", padx=5, pady=10
        )

        table_frame = tk.Frame(self.root)
        table_frame.place(x=370, y=15, width=760, height=360)

        columns = (
            "code",
            "name",
            "address",
            "branches",
            "staff",
            "cost",
            "vol",
            "date",
        )
        self.tree = ttk.Treeview(
            table_frame, columns=columns, show="headings", selectmode="browse"
        )

        self.tree.heading("code", text="Код")
        self.tree.heading("name", text="Название")
        self.tree.heading("address", text="Адрес")
        self.tree.heading("branches", text="Филиалы")
        self.tree.heading("staff", text="Персонал")
        self.tree.heading("cost", text="Стоим. обор.")
        self.tree.heading("vol", text="Объем прод.")
        self.tree.heading("date", text="Дата рег.")

        self.tree.column("code", width=40, anchor="center")
        self.tree.column("name", width=100)
        self.tree.column("address", width=120)
        self.tree.column("branches", width=60, anchor="center")
        self.tree.column("staff", width=70, anchor="center")
        self.tree.column("cost", width=90)
        self.tree.column("vol", width=90)
        self.tree.column("date", width=80, anchor="center")

        scrollbar = ttk.Scrollbar(
            table_frame, orient="vertical", command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        control_frame = tk.LabelFrame(
            self.root,
            text="Операции (по 3 SQL-запроса на действие)",
            bg="#f4f4f4",
            font=("Arial", 10, "bold"),
        )
        control_frame.place(x=15, y=390, width=1115, height=230)

        tk.Label(
            control_frame,
            text="РЕДАКТИРОВАНИЕ:",
            bg="#f4f4f4",
            font=("Arial", 9, "bold"),
        ).grid(row=0, column=0, columnspan=3, sticky="w", padx=5, pady=2)
        tk.Button(
            control_frame,
            text="1: Обновить ВСЕ поля записи по Коду",
            bg="#2196F3",
            fg="white",
            command=lambda: self.edit_record(1),
        ).grid(row=1, column=0, padx=5, pady=2, sticky="ew")
        tk.Button(
            control_frame,
            text="2: Сбросить филиалы в 0 (если объем < 4млн)",
            bg="#2196F3",
            fg="white",
            command=lambda: self.edit_record(2),
        ).grid(row=1, column=1, padx=5, pady=2, sticky="ew")
        tk.Button(
            control_frame,
            text="3: Увеличить персонал на 10% (обор > 3млн)",
            bg="#2196F3",
            fg="white",
            command=lambda: self.edit_record(3),
        ).grid(row=1, column=2, padx=5, pady=2, sticky="ew")

        tk.Label(
            control_frame,
            text="УДАЛЕНИЕ:",
            bg="#f4f4f4",
            font=("Arial", 9, "bold"),
        ).grid(row=2, column=0, columnspan=3, sticky="w", padx=5, pady=2)
        tk.Button(
            control_frame,
            text="1: Удалить выбранное по Коду",
            bg="#f44336",
            fg="white",
            command=lambda: self.delete_record(1),
        ).grid(row=3, column=0, padx=5, pady=2, sticky="ew")
        tk.Button(
            control_frame,
            text="2: Удалить где персонал < 5000",
            bg="#f44336",
            fg="white",
            command=lambda: self.delete_record(2),
        ).grid(row=3, column=1, padx=5, pady=2, sticky="ew")
        tk.Button(
            control_frame,
            text="3: Удалить без филиалов (филиалы=0)",
            bg="#f44336",
            fg="white",
            command=lambda: self.delete_record(3),
        ).grid(row=3, column=2, padx=5, pady=2, sticky="ew")

        tk.Label(
            control_frame,
            text="ПОИСК И ФИЛЬТРАЦИЯ:",
            bg="#f4f4f4",
            font=("Arial", 9, "bold"),
        ).grid(row=4, column=0, columnspan=3, sticky="w", padx=5, pady=2)
        tk.Button(
            control_frame,
            text="1: Объем продукции > 5 000 000",
            bg="#FF9800",
            fg="white",
            command=lambda: self.search_records(1),
        ).grid(row=5, column=0, padx=5, pady=2, sticky="ew")
        tk.Button(
            control_frame,
            text="2: Поиск по названию (из поля слева)",
            bg="#FF9800",
            fg="white",
            command=lambda: self.search_records(2),
        ).grid(row=5, column=1, padx=5, pady=2, sticky="ew")
        tk.Button(
            control_frame,
            text="3: Регистрация после 2000 года",
            bg="#FF9800",
            fg="white",
            command=lambda: self.search_records(3),
        ).grid(row=5, column=2, padx=5, pady=2, sticky="ew")

        tk.Button(
            control_frame,
            text="Сбросить фильтры поиска (Показать все предприятия)",
            bg="#9E9E9E",
            fg="white",
            command=self.refresh_table,
        ).grid(row=6, column=0, columnspan=3, padx=5, pady=5, sticky="ew")

    def refresh_table(self, rows=None):
        for item in self.tree.get_children():
            self.tree.delete(item)
        if rows is None:
            self.cursor.execute("SELECT * FROM enterprises")
            rows = self.cursor.fetchall()
        for row in rows:
            self.tree.insert("", "end", values=row)

    def on_tree_select(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        values = self.tree.item(selected)["values"]
        keys = [
            "code",
            "name",
            "address",
            "branches",
            "staff",
            "eq_cost",
            "volume",
            "date",
        ]
        for i, key in enumerate(keys):
            self.entries[key].delete(0, tk.END)
            self.entries[key].insert(0, str(values[i]))

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def add_record(self):
        try:
            name = self.entries["name"].get().strip()
            address = self.entries["address"].get().strip()
            if not name or not address:
                raise ValueError("Название и адрес не могут быть пустыми!")

            branches = int(self.entries["branches"].get())
            staff = int(self.entries["staff"].get())
            eq_cost = float(self.entries["eq_cost"].get())
            volume = float(self.entries["volume"].get())
            date_str = self.entries["date"].get().strip()
            datetime.strptime(date_str, "%Y-%m-%d")

            self.cursor.execute(
                """
                INSERT INTO enterprises (name, address, branches, staff, equipment_cost, production_volume, reg_date)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
                (name, address, branches, staff, eq_cost, volume, date_str),
            )
            self.conn.commit()
            messagebox.showinfo("Успех", "Предприятие успешно добавлено!")
            self.clear_entries()
            self.refresh_table()
        except ValueError as e:
            messagebox.showerror(
                "Ошибка ввода", f"Неверный формат данных!\nДетали: {e}"
            )

    def edit_record(self, query_num):
        try:
            if query_num == 1:
                code = self.entries["code"].get()
                if not code:
                    messagebox.showwarning(
                        "Внимание", "Сначала выберите строку в таблице!"
                    )
                    return
                name = self.entries["name"].get().strip()
                address = self.entries["address"].get().strip()
                branches = int(self.entries["branches"].get())
                staff = int(self.entries["staff"].get())
                eq_cost = float(self.entries["eq_cost"].get())
                volume = float(self.entries["volume"].get())
                date_str = self.entries["date"].get().strip()
                datetime.strptime(date_str, "%Y-%m-%d")

                self.cursor.execute(
                    """
                    UPDATE enterprises 
                    SET name=?, address=?, branches=?, staff=?, equipment_cost=?, production_volume=?, reg_date=?
                    WHERE code=?
                """,
                    (
                        name,
                        address,
                        branches,
                        staff,
                        eq_cost,
                        volume,
                        date_str,
                        int(code),
                    ),
                )
            elif query_num == 2:
                self.cursor.execute(
                    "UPDATE enterprises SET branches = 0 WHERE production_volume < 4000000.0"
                )
            elif query_num == 3:
                self.cursor.execute(
                    "UPDATE enterprises SET staff = CAST(staff * 1.1 AS INTEGER) WHERE equipment_cost > 3000000.0"
                )

            self.conn.commit()
            messagebox.showinfo("Успех", f"Запрос №{query_num} выполнен!")
            self.refresh_table()
        except ValueError as e:
            messagebox.showerror("Ошибка", f"Неверные данные: {e}")

    def delete_record(self, query_num):
        try:
            if query_num == 1:
                code = self.entries["code"].get()
                if not code:
                    messagebox.showwarning(
                        "Внимание", "Выберите строку для удаления!"
                    )
                    return
                self.cursor.execute(
                    "DELETE FROM enterprises WHERE code = ?", (int(code),)
                )
            elif query_num == 2:
                self.cursor.execute("DELETE FROM enterprises WHERE staff < 5000")
            elif query_num == 3:
                self.cursor.execute("DELETE FROM enterprises WHERE branches = 0")

            self.conn.commit()
            self.clear_entries()
            self.refresh_table()
            messagebox.showinfo("Успех", "Удаление выполнено!")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def search_records(self, query_num):
        try:
            if query_num == 1:
                self.cursor.execute(
                    "SELECT * FROM enterprises WHERE production_volume > 5000000.0"
                )
            elif query_num == 2:
                search_name = self.entries["name"].get().strip()
                if not search_name:
                    messagebox.showwarning(
                        "Внимание", "Введите текст в поле 'Наименование'!"
                    )
                    return
                self.cursor.execute(
                    "SELECT * FROM enterprises WHERE name LIKE ?",
                    (f"%{search_name}%",),
                )
            elif query_num == 3:
                self.cursor.execute(
                    "SELECT * FROM enterprises WHERE reg_date >= '2000-01-01'"
                )

            filtered_rows = self.cursor.fetchall()
            self.refresh_table(filtered_rows)
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = IndustryApp(root)
    root.mainloop()
