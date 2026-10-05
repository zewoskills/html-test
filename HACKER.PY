import os
import random
import time
from datetime import datetime, timedelta


GREEN = '\033[32m'
BOLD = '\033[1m'
RESET = '\033[0m'

class HackerConsole:
    def __init__(self):
        self.level = 1
        self.xp = 0
        self.missions = 0
        self.success = 0
        self.is_running = True

    def set_color(self):
        print(f"{GREEN}{BOLD}", end="")

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def check_level_up(self):
        required_xp = self.level * 100
        if self.xp >= required_xp:
            self.xp -= required_xp
            self.level += 1
            print(f"\n>>> ACCESS LEVEL INCREASED <<<")
            print(f"Новый уровень доступа: {self.level}")
            print("Открыты новые возможности систем.\n")

    def trigger_random_event(self):
        if random.random() < 0.2:
            print(f"\n!!! WARNING !!!")
            print("Обнаружена подозрительная активность.")
            print("Система заблокируется через 10 секунд.")
            

            a = random.randint(10, 50)
            b = random.randint(5, 20)
            c = random.randint(2, 5)
            correct_answer = a + (b * c)
            
            print(f"Введите код подтверждения: {a} + {b} * {c} = ?")
            start_time = time.time()
            
            try:
                answer = input(">> ")
                if time.time() - start_time > 10:
                    print("Время вышло! Доступ заблокирован (штраф -50 XP).")
                    self.xp = max(0, self.xp - 50)
                elif int(answer) == correct_answer:
                    print("Подтверждение принято. Система работает в штатном режиме.")
                    self.xp += 30
                    self.check_level_up()
                else:
                    print("Неверный код! Штраф -50 XP.")
                    self.xp = max(0, self.xp - 50)
            except ValueError:
                print("Ошибка ввода! Штраф -50 XP.")
                self.xp = max(0, self.xp - 50)

    def scan(self):
        print("\nСканирование сети...\n")
        time.sleep(1)
        count = random.randint(3, 6)
        for _ in range(count):
            sys_id = f"{random.choice(['SERVER', 'NODE', 'UNKNOWN', 'PROXY'])}-{random.randint(10, 99)}"
            status = random.choice(['ONLINE', 'OFFLINE', 'ENCRYPTED', 'UNREACHABLE'])
            
            if status == 'ONLINE':
                print(f"[+] {sys_id:<12} {status}")
            elif status == 'OFFLINE':
                print(f"[-] {sys_id:<12} {status}")
            else:
                print(f"[?] {sys_id:<12} {status}")
            time.sleep(0.4) 
        
        self.xp += 20
        self.missions += 1
        self.success += 1
        print("\nСканирование завершено. Получено +20 XP.")
        self.check_level_up()

    def decode(self):
        words = ["HELLO WORLD", "SYSTEM HACK", "ACCESS GRANTED", "FIREWALL DOWN", "CYBER PUNK"]
        word = random.choice(words)
        shift = random.randint(2, 5)
        
        encrypted = ""
        for char in word:
            if char.isalpha():
                base = ord('A')
                encrypted += chr((ord(char) - base + shift) % 26 + base)
            else:
                encrypted += char
                
        print("\nЗАШИФРОВАННОЕ СООБЩЕНИЕ:\n")
        print(f"  {encrypted}\n")
        
        answer = input("Введите расшифрованный текст: ").upper()
        self.missions += 1
        
        if answer == word:
            print("Расшифровка успешна! Получено +50 XP.")
            self.xp += 50
            self.success += 1
            self.check_level_up()
        else:
            print(f"Ошибка. Правильный ответ: {word}")

    def logs(self):
        events = [
            "Connection established",
            "Unknown user detected",
            "Firewall activated",
            "Access attempt blocked",
            "Data packet intercepted",
            "Encryption key generated"
        ]
        print("\nSYSTEM LOGS:")
        now = datetime.now()
        for i in range(5, 0, -1):
            log_time = now - timedelta(seconds=random.randint(10, 300) * i)
            event = random.choice(events)
            print(f"[{log_time.strftime('%H:%M:%S')}] {event}")
            time.sleep(0.2)
        print()

    def show_status(self):
        print("\n╔══════════════════════╗")
        print("║ PLAYER STATUS        ║")
        print("╠══════════════════════╣")
        print(f"║ Level:     {self.level:<9} ║")
        print(f"║ XP:        {self.xp:<9} ║")
        print(f"║ Missions:  {self.missions:<9} ║")
        print(f"║ Success:   {self.success:<9} ║")
        print("╚══════════════════════╝\n")

    def show_help(self):
        print("\nДоступные команды:")
        print("  scan   - сканирование сети")
        print("  decode - дешифровка данных")
        print("  logs   - просмотр системных журналов")
        print("  status - статистика профиля")
        print("  help   - список команд")
        print("  exit   - выход из системы\n")

    def run(self):
        self.set_color()
        self.clear()
        print("╔══════════════════════════════════╗")
        print("║       CYBER TERMINAL v1.0        ║")
        print("╚══════════════════════════════════╝")
        print("\nДобро пожаловать, оператор.")
        print(f"Ваш уровень доступа: {self.level}")
        self.show_help()

        while self.is_running:
            try:
                cmd = input("\nroot@cyber-terminal:~# ").strip().lower()
                
                if cmd == 'scan':
                    self.scan()
                    self.trigger_random_event()
                elif cmd == 'decode':
                    self.decode()
                    self.trigger_random_event()
                elif cmd == 'logs':
                    self.logs()
                elif cmd == 'status':
                    self.show_status()
                elif cmd == 'help':
                    self.show_help()
                elif cmd == 'exit':
                    print("Отключение от системы...")
                    time.sleep(1)
                    print(RESET) # Renk sıfırlama
                    self.clear()
                    self.is_running = False
                elif cmd == "":
                    continue
                else:
                    print("Неизвестная команда. Введите 'help' для списка команд.")
            except KeyboardInterrupt:
                print("\nЭкстренное отключение от системы...")
                print(RESET)
                self.is_running = False

if __name__ == "__main__":
    game = HackerConsole()
    game.run()