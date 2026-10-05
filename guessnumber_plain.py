import random
import tkinter as tk


BACKGROUND = "#FFF7ED"
CARD = "#FFFFFF"
TEXT = "#3F2D20"
ACCENT = "#EA580C"
ACCENT_ACTIVE = "#F97316"
SECONDARY = "#0F766E"
SECONDARY_ACTIVE = "#14B8A6"
MUTED = "#78716C"
SUCCESS = "#15803D"
ERROR = "#B91C1C"


def check_guess():
    global attempts

    try:
        guess = int(entry_guess.get())
    except ValueError:
        result_label.config(text="Введите целое число.", fg=ERROR)
        entry_guess.delete(0, tk.END)
        return

    if not 1 <= guess <= 100:
        result_label.config(text="Введите число от 1 до 100.", fg=ERROR)
        entry_guess.delete(0, tk.END)
        return

    attempts += 1
    attempts_label.config(text=f"Попытка: {attempts}")

    if guess < secret_number:
        result_label.config(text="Мало. Попробуйте число больше.", fg=ACCENT)
    elif guess > secret_number:
        result_label.config(text="Много. Попробуйте число меньше.", fg=ACCENT)
    else:
        result_label.config(
            text=f"Победа! Вы угадали за {attempts} попыток.",
            fg=SUCCESS,
        )
        entry_guess.config(state="disabled")
        check_button.config(state="disabled")

    entry_guess.delete(0, tk.END)


def reset_game():
    global secret_number, attempts

    secret_number = random.randint(1, 100)
    attempts = 0
    entry_guess.config(state="normal")
    check_button.config(state="normal")
    entry_guess.delete(0, tk.END)
    result_label.config(text="", fg=TEXT)
    attempts_label.config(text="Попытка: 0")
    entry_guess.focus_set()


root = tk.Tk()
root.title("Угадай число")
root.geometry("760x560")
root.configure(bg=BACKGROUND)
root.resizable(False, False)

secret_number = random.randint(1, 100)
attempts = 0

main_frame = tk.Frame(root, bg=CARD, padx=48, pady=38)
main_frame.pack(padx=35, pady=35, fill="both", expand=True)

title_label = tk.Label(
    main_frame,
    text="Угадай число",
    font=("Arial", 28, "bold"),
    bg=CARD,
    fg=TEXT,
)
title_label.pack(pady=(0, 5))

subtitle_label = tk.Label(
    main_frame,
    text="Я загадал число от 1 до 100",
    font=("Arial", 15),
    bg=CARD,
    fg=MUTED,
)
subtitle_label.pack(pady=(0, 14))

entry_guess = tk.Entry(
    main_frame,
    font=("Arial", 24),
    width=12,
    justify="center",
    bg="#FFEDD5",
    fg=TEXT,
    insertbackground=TEXT,
    relief="flat",
)
entry_guess.pack(pady=8, ipady=8)

check_button = tk.Button(
    main_frame,
    text="Проверить",
    font=("Arial", 15, "bold"),
    bg=ACCENT,
    fg="white",
    activebackground=ACCENT_ACTIVE,
    activeforeground="white",
    relief="flat",
    padx=26,
    pady=10,
    command=check_guess,
)
check_button.pack(pady=(14, 8))

result_label = tk.Label(
    main_frame,
    text="",
    font=("Arial", 15, "bold"),
    bg=CARD,
    fg=TEXT,
)
result_label.pack(pady=8)

attempts_label = tk.Label(
    main_frame,
    text="Попытка: 0",
    font=("Arial", 14),
    bg=CARD,
    fg=MUTED,
)
attempts_label.pack(pady=8)

reset_button = tk.Button(
    main_frame,
    text="Новая игра",
    font=("Arial", 14),
    bg=SECONDARY,
    fg="white",
    activebackground=SECONDARY_ACTIVE,
    activeforeground="white",
    relief="flat",
    padx=22,
    pady=8,
    command=reset_game,
)
reset_button.pack(pady=(8, 0))

root.bind("<Return>", lambda event: check_guess())
entry_guess.focus_set()
root.mainloop()
