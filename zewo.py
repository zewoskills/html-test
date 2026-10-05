# # import re

# # EMAIL_REGEX = re.compile(
# #     r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
# # )

# # def is_valid_email(email: str) -> bool:
# #     if not isinstance(email, str):
# #         return False
# #     return bool(EMAIL_REGEX.fullmatch(email.strip()))


# # print(is_valid_email("test@example.com"))
# # print(is_valid_email("wrong-email"))



















# # def is_valid_email(email: str | None) -> bool:
# #     if not isinstance(email, str):
# #         return False

# #     cleaned_email = email.strip()

# #     if not cleaned_email or cleaned_email.count("@") != 1:
# #         return False

# #     username, domain = cleaned_email.split("@")

# #     if not username or not domain:
# #         return False

# #     allowed_username_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._+-")
# #     if any(character not in allowed_username_characters for character in username):
# #         return False

# #     if "." not in domain or domain.startswith(".") or domain.endswith(".") or ".." in domain:
# #         return False

# #     domain_labels = domain.split(".")
# #     if any(not label for label in domain_labels):
# #         return False

# #     top_level_domain = domain_labels[-1]
# #     if len(top_level_domain) < 2 or not top_level_domain.isalpha():
# #         return False

# #     allowed_domain_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-.")
# #     if any(character not in allowed_domain_characters for character in domain):
# #         return False

# #     return True


# # test_cases = [
# #     ("", False),
# #     (" ", False),
# #     (None, False),
# #     ("user@domain", False),
# #     ("user@.domain.com", False),
# #     ("user@domain.", False),
# #     ("user@domain.c", False),
# #     ("user@sub.domain.com", True),
# #     ("user.name+tag@example.ru", True)
# # ]

# # for email, expected in test_cases:
# #     assert is_valid_email(email) == expected, f"Ошибка: {email}"
# # print("Все правильно.")






















# import re

# # Шаблон для локальной части email (до '@')
# LOCAL_PART_PATTERN = re.compile(r"^[a-zA-Z0-9_.+-]+$")
# # Шаблон для доменной части email (после '@')
# DOMAIN_PART_PATTERN = re.compile(r"^[a-zA-Z0-9-.]+$")


# class EmailValidationResult:
#     # Хранит результат проверки: валиден ли email и список ошибок
#     def __init__(self, is_valid: bool, errors: list[str]):
#         self.is_valid = is_valid
#         self.errors = errors

#     def __repr__(self):
#         return f"EmailValidationResult(is_valid={self.is_valid}, errors={self.errors})"


# def validate_email(email: object) -> EmailValidationResult:
#     errors: list[str] = []

#     # Проверка типа данных
#     if not isinstance(email, str):
#         return EmailValidationResult(False, ["Значение должно быть строкой."])

#     cleaned_email = email.strip()

#     # Проверка на пустую строку
#     if not cleaned_email:
#         return EmailValidationResult(False, ["Email не может быть пустым."])

#     # Проверка количества символов '@'
#     at_symbol_count = cleaned_email.count("@")
#     if at_symbol_count == 0:
#         return EmailValidationResult(False, ["Отсутствует символ '@'."])
#     if at_symbol_count > 1:
#         return EmailValidationResult(False, ["Email содержит более одного символа '@'."])

#     local_part, domain_part = cleaned_email.split("@")

#     # Проверка локальной части
#     if not local_part:
#         errors.append("Имя пользователя (до '@') не может быть пустым.")
#     elif not LOCAL_PART_PATTERN.fullmatch(local_part):
#         errors.append("Имя пользователя содержит недопустимые символы (разрешены буквы, цифры, '.', '_', '+', '-').")

#     # Проверка доменной части
#     if not domain_part:
#         errors.append("Доменная часть (после '@') не может быть пустой.")
#         return EmailValidationResult(False, errors)

#     if not DOMAIN_PART_PATTERN.fullmatch(domain_part):
#         errors.append("Домен содержит недопустимые символы.")

#     # Проверка наличия точки и корректности структуры домена
#     if "." not in domain_part:
#         errors.append("Домен должен содержать точку.")
#     else:
#         if domain_part.startswith("."):
#             errors.append("Домен не может начинаться с точки.")
#         if domain_part.endswith("."):
#             errors.append("Домен не может заканчиваться точкой.")

#         domain_labels = domain_part.split(".")

#         # Проверка длины зоны домена (TLD)
#         top_level_domain = domain_labels[-1]
#         if len(top_level_domain) < 2:
#             errors.append(f"Зона домена (.{top_level_domain}) слишком короткая (минимум 2 символа).")

#         # Проверка на пустые поддомены (подряд идущие точки)
#         if any(label == "" for label in domain_labels[1:-1]):
#             errors.append("Домен содержит пустые поддомены (подряд идущие точки).")

#     return EmailValidationResult(len(errors) == 0, errors)


# test_inputs = [
#     "user@example.com",
#     "",
#     " ",
#     "plainaddress",
#     "user@domain",
#     "user@.com",
#     "user@domain.",
#     "user@domain.c",
#     "user@@domain.com",
#     "user name@domain.com",
#     "user@sub..domain.com",
# ]

# for item in test_inputs:
#     result = validate_email(item)
#     status = "Валиден" if result.is_valid else f"Ошибки: {result.errors}"
#     print(f"'{item}' -> {status}")
































import tkinter
from tkinter import messagebox
import sqlite3


class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Менеджер задач")
        self.root.geometry("400x450")

        self.connection = sqlite3.connect("tasks.db")
        self.cursor = self.connection.cursor()
        self.create_table()

        self.entry = tkinter.Entry(root, width=35, font=("Arial", 12))
        self.entry.pack(pady=10)

        self.add_button = tkinter.Button(root, text="Добавить задачу", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tkinter.Listbox(root, width=45, height=15, font=("Arial", 11))
        self.task_listbox.pack(pady=10)

        self.done_button = tkinter.Button(root, text="Отметить выполненной", command=self.mark_done)
        self.done_button.pack(pady=5)

        self.delete_button = tkinter.Button(root, text="Удалить задачу", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.load_tasks()

    def create_table(self):
        with self.connection:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    is_done INTEGER DEFAULT 0
                )
            """)

    def load_tasks(self):
        self.task_listbox.delete(0, tkinter.END)
        with self.connection:
            self.cursor.execute("SELECT id, title, is_done FROM tasks")
            tasks = self.cursor.fetchall()

        for task_id, title, is_done in tasks:
            prefix = "[Готово] " if is_done else "[В работе] "
            self.task_listbox.insert(tkinter.END, f"{prefix}{title}")

    def add_task(self):
        title = self.entry.get().strip()
        if not title:
            messagebox.showwarning("Предупреждение", "Введите текст задачи")
            return

        with self.connection:
            self.cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))

        self.entry.delete(0, tkinter.END)
        self.load_tasks()

    def get_selected_task_id(self):
        selection = self.task_listbox.curselection()
        if not selection:
            messagebox.showwarning("Предупреждение", "Выберите задачу из списка")
            return None

        with self.connection:
            self.cursor.execute("SELECT id FROM tasks ORDER BY id")
            all_ids = [row[0] for row in self.cursor.fetchall()]

        return all_ids[selection[0]]

    def mark_done(self):
        task_id = self.get_selected_task_id()
        if task_id is None:
            return

        with self.connection:
            self.cursor.execute("UPDATE tasks SET is_done = 1 WHERE id = ?", (task_id,))

        self.load_tasks()

    def delete_task(self):
        task_id = self.get_selected_task_id()
        if task_id is None:
            return

        with self.connection:
            self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

        self.load_tasks()


if __name__ == "__main__":
    root = tkinter.Tk()
    app = TaskManager(root)
    root.mainloop() 




# import tkinter

# task_list = []

# root = tkinter.Tk()
# root.title("Список задач (ibo)")
# root.geometry("650x700")

# entry = tkinter.Entry(root, width=30)
# entry.pack(pady=10)


# def add_task():
#     task_text = entry.get()
#     if task_text != "":
#         task_list.append(task_text)
#         listbox.insert(tkinter.END, task_text)
#         entry.delete(0, tkinter.END)


# def delete_task():
#     selected = listbox.curselection()
#     if selected:
#         index = selected[0]
#         listbox.delete(index)
#         task_list.pop(index)


# add_button = tkinter.Button(root, text="Добавить", command=add_task)
# add_button.pack(pady=5)

# listbox = tkinter.Listbox(root, width=35, height=15)
# listbox.pack(pady=10)

# delete_button = tkinter.Button(root, text="Удалить", command=delete_task)
# delete_button.pack(pady=5)

# root.mainloop()