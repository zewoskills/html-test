import random
import string


def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    pools = []
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_lower:
        pools.append(string.ascii_lowercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append('!@#$%^&*()-_=+')

    if not pools:
        raise ValueError("нужно выбрать хотя бы один тип символов")

    if length < len(pools):
        raise ValueError(
            f"длина пароля ({length}) меньше количества выбранных типов "
            f"символов ({len(pools)}) — увеличьте длину или уберите тип"
        )

    all_chars = ''.join(pools)
    # гарантируем, что каждый выбранный тип символов встретится хотя бы раз
    password_chars = [random.choice(pool) for pool in pools]
    remaining = length - len(password_chars)
    password_chars += [random.choice(all_chars) for _ in range(remaining)]
    random.shuffle(password_chars)
    return ''.join(password_chars)


def ask_yes_no(prompt):
    while True:
        answer = input(prompt + " (y/n): ").strip().lower()
        if answer in ('y', 'yes', 'д', 'да'):
            return True
        if answer in ('n', 'no', 'н', 'нет'):
            return False
        print("Введите y или n")


def main():
    print("=== Генератор паролей ===")
    while True:
        try:
            length = int(input("Длина пароля: "))
            if length <= 0:
                print("Длина должна быть положительным числом")
                continue
            break
        except ValueError:
            print("Введите число")

    use_upper = ask_yes_no("Использовать заглавные буквы?")
    use_lower = ask_yes_no("Использовать строчные буквы?")
    use_digits = ask_yes_no("Использовать цифры?")
    use_symbols = ask_yes_no("Использовать спецсимволы?")

    try:
        count = int(input("Сколько паролей сгенерировать? "))
        if count <= 0:
            count = 1
    except ValueError:
        count = 1

    try:
        for i in range(count):
            pwd = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
            print(f"Пароль {i + 1}: {pwd}")
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()