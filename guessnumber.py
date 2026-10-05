import tkinter as tk
import random

class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Угадай число")
        self.root.geometry("400x350")
        self.root.config(bg="#2b2b2b")
        self.root.resizable(False, False)
        
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.is_animating = False
        
        # Элементы интерфейса
        self.title_label = tk.Label(root, text="Загадай число от 1 до 100\nПопробуй угадать!", 
                                    font=("Helvetica", 14, "bold"), bg="#2b2b2b", fg="white")
        self.title_label.pack(pady=20)
        
        self.entry = tk.Entry(root, font=("Helvetica", 24), justify="center", width=5)
        self.entry.pack(pady=10)
        
        self.check_button = tk.Button(root, text="Проверить", font=("Helvetica", 12, "bold"), 
                                      bg="#4CAF50", fg="white", activebackground="#45a049",
                                      command=self.check_guess)
        self.check_button.pack(pady=15)
        
        self.feedback_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#2b2b2b", fg="yellow")
        self.feedback_label.pack(pady=10)

        self.reset_button = tk.Button(root, text="Играть снова", font=("Helvetica", 10), 
                                      command=self.reset_game)
        self.reset_button.pack(pady=10)
        self.reset_button.pack_forget() # Скрываем кнопку до победы
        
        # Привязка клавиши Enter к проверке
        self.root.bind('<Return>', lambda event: self.check_guess())

    def check_guess(self):
        if self.is_animating:
            return

        try:
            guess = int(self.entry.get())
            self.attempts += 1
            
            if guess < self.target_number:
                self.feedback_label.config(text="Слишком мало! Бери выше ⬆️", fg="#ff6b6b")
                self.shake_window()
            elif guess > self.target_number:
                self.feedback_label.config(text="Слишком много! Бери ниже ⬇️", fg="#ff6b6b")
                self.shake_window()
            else:
                self.feedback_label.config(text=f"Бинго! Ты угадал за {self.attempts} попыток 🏆", fg="#51cf66")
                self.check_button.config(state="disabled")
                self.entry.config(state="disabled")
                self.win_animation()
                
        except ValueError:
            self.feedback_label.config(text="Ошибка! Введи целое число.", fg="red")
            self.shake_window()
            
        self.entry.delete(0, tk.END)

    def shake_window(self):
        # Анимация тряски окна при ошибке
        self.is_animating = True
        x = self.root.winfo_x()
        y = self.root.winfo_y()
        
        # Смещения для тряски
        offsets = [15, -15, 10, -10, 5, -5, 0]
        delay = 0
        
        for offset in offsets:
            self.root.after(delay, lambda o=offset: self.root.geometry(f"+{x+o}+{y}"))
            delay += 30
            
        self.root.after(delay, self.unlock_animation)

    def win_animation(self):
        # Анимация изменения цвета фона при победе
        self.is_animating = True
        colors = ["#FF9999", "#99FF99", "#9999FF", "#FFFF99", "#FF99FF", "#2b2b2b"]
        delay = 0
        
        for _ in range(3): # Повторяем цикл цветов 3 раза
            for color in colors:
                self.root.after(delay, lambda c=color: self.change_bg(c))
                delay += 150
                
        self.root.after(delay, self.show_reset_button)
        self.root.after(delay, self.unlock_animation)

    def change_bg(self, color):
        self.root.config(bg=color)
        self.title_label.config(bg=color)
        self.feedback_label.config(bg=color)

    def show_reset_button(self):
        self.reset_button.pack(pady=10)

    def unlock_animation(self):
        self.is_animating = False

    def reset_game(self):
        # Сброс игры до начального состояния
        self.target_number = random.randint(1, 100)
  
import tkinter as tk
import random

def check_guess():
    global attempts, secret_number, cheated

    # Получаем текст из поля ввода
    try:
        guess = int(entry_guess.get())
    except ValueError:
        lbl_result.config(text="Введи число!", fg="red")
        shake_window()
        return

    attempts += 1
    lbl_attempts.config(text=f"Попытка: {attempts}")

    # Проверяем число
    if guess < secret_number:
        lbl_result.config(text="Мало! Бери выше.", fg="red")
        shake_window()
    elif guess > secret_number:
        lbl_result.config(text="Много! Бери ниже.", fg="red")
        shake_window()
    else:
        lbl_result.config(text=f"🎉 УГАДАЛ за {attempts} попыток! 🎉", fg="green")
        btn_check.config(state="disabled")
        btn_cheat.config(state="disabled")
        entry_guess.config(state="disabled")
        win_animation(20) # Запуск анимации победы (20 кадров)

        entry_guess.delete(0, tk.END)
        return

    # Компьютер жульничает после каждого неверного числового ответа.
    secret_number = random.randint(1, 100)
    cheated = True


def accuse_computer():
    """Проверяет обвинение игрока в жульничестве."""
    if cheated:
        lbl_result.config(text="🎉 Ты поймал компьютер! Ты выиграл! 🎉", fg="#2DD4BF")
        win_animation(20)
    else:
        lbl_result.config(text="Компьютер не жульничал. Ты проиграл.", fg="#FF6B6B")

    btn_check.config(state="disabled")
    btn_cheat.config(state="disabled")
    entry_guess.config(state="disabled")


def reset_game():
    global secret_number, attempts, cheated

    secret_number = random.randint(1, 100)
    attempts = 0
    cheated = False
    entry_guess.config(state="normal")
    btn_check.config(state="normal")
    btn_cheat.config(state="normal")
    entry_guess.delete(0, tk.END)
    lbl_result.config(text="", fg="#E6FFFA", font=("Arial", 14, "bold"))
    lbl_attempts.config(text="Попытка: 0")

def shake_window(c=0):
    # Анимация: тряска окна при ошибке
    if c < 6:
        x = root.winfo_x() + (10 if c % 2 == 0 else -10)
        y = root.winfo_y()
        root.geometry(f"+{x}+{y}")
        root.after(40, shake_window, c+1)

def win_animation(c):
    # Анимация: пульсация и смена цвета текста при победе
    if c > 0:
        colors = ["green", "blue", "magenta", "orange", "red"]
        lbl_result.config(fg=colors[c % len(colors)])
        
        # Меняем размер шрифта
        size = 14 + (c % 3) * 2
        lbl_result.config(font=("Arial", size, "bold"))
        
        root.after(100, win_animation, c-1)
    else:
        lbl_result.config(fg="green", font=("Arial", 16, "bold"))

# Создаем главное окно
root = tk.Tk()
root.title("Угадай число")
root.geometry("350x250")
root.config(bg="#17212B")

# Компьютер загадывает число от 1 до 100
secret_number = random.randint(1, 100)
attempts = 0
cheated = False

# Текст сверху
title_label = tk.Label(
    root,
    text="Я загадал число от 1 до 100.",
    font=("Arial", 12, "bold"),
    bg="#17212B",
    fg="#E6FFFA",
)
title_label.pack(pady=15)

# Поле для ввода
entry_guess = tk.Entry(
    root,
    font=("Arial", 16),
    width=10,
    justify="center",
    bg="#F4F7F8",
    fg="#17212B",
    insertbackground="#17212B",
)
entry_guess.pack(pady=10)

# Кнопка проверки
btn_check = tk.Button(
    root,
    text="Проверить",
    font=("Arial", 12, "bold"),
    bg="#2DD4BF",
    fg="#102027",
    activebackground="#5EEAD4",
    activeforeground="#102027",
    command=check_guess,
)
btn_check.pack(pady=10)

# Кнопка обвинения компьютера в жульничестве
btn_cheat = tk.Button(
    root,
    text="Поймал на жульничестве!",
    font=("Arial", 10),
    bg="#F59E0B",
    fg="#17212B",
    activebackground="#FBBF24",
    command=accuse_computer,
)
btn_cheat.pack(pady=5)

# Текст результата (сначала пустой)
lbl_result = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#17212B", fg="#E6FFFA")
lbl_result.pack(pady=10)

# Счётчик попыток
lbl_attempts = tk.Label(root, text="Попытка: 0", font=("Arial", 11), bg="#17212B", fg="#A7C4C2")
lbl_attempts.pack(pady=5)

# Кнопка сброса игры
btn_reset = tk.Button(
    root,
    text="Reset",
    font=("Arial", 11),
    bg="#334155",
    fg="#F8FAFC",
    activebackground="#475569",
    activeforeground="#F8FAFC",
    command=reset_game,
)
btn_reset.pack(pady=5)

# Ставим окно по центру экрана при запуске
root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) // 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) // 2
root.geometry(f"+{x}+{y}")

# Запускаем программу
root.mainloop()