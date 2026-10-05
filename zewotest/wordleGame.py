"""Простая версия игры Wordle."""


class WordleGame:
    """Класс для игры Wordle с проверкой попыток и подсказками."""

    def __init__(self, secret_word):
        """Инициализирует игру с загаданным словом и ограничением по попыткам."""
        # Загаданное слово должно быть строкой.
        if not isinstance(secret_word, str):
            raise ValueError("Секретное слово должно быть строкой.")

        # Приводим слово к нижнему регистру, чтобы сравнение было регистронезависимым.
        self.secret_word = secret_word.lower()

        # Максимум попыток для игрока.
        self.max_attempts = 6

        # Список всех попыток и их подсказок.
        self.feedback_history = []

    def guess(self, word):
        """Проверяет попытку игрока и возвращает подсказки для каждой буквы."""
        # Проверяем, что попытка является строкой.
        if not isinstance(word, str):
            raise ValueError("Попытка должна быть строкой.")

        # Приводим к нижнему регистру для сравнения.
        guessed_word = word.lower()

        # Если количество букв не совпадает, выбрасываем ошибку.
        if len(guessed_word) != len(self.secret_word):
            raise ValueError("Количество букв в попытке не совпадает с загаданным словом.")

        # Создаём список подсказок по умолчанию.
        result = ["absent"] * len(self.secret_word)

        # Сначала отмечаем правильные буквы на правильных местах.
        for index in range(len(self.secret_word)):
            if guessed_word[index] == self.secret_word[index]:
                result[index] = "correct"

        # Затем проверяем оставшиеся буквы: если буква есть в слове, но не на этом месте.
        for index in range(len(self.secret_word)):
            if result[index] == "correct":
                continue

            if guessed_word[index] in self.secret_word:
                result[index] = "present"

        # Сохраняем историю попыток.
        self.feedback_history.append({
            "guess": guessed_word,
            "feedback": result.copy(),
        })

        return result

    def get_feedback(self):
        """Возвращает историю всех попыток вместе с подсказками."""
        # Возвращаем список всех попыток и результатов.
        return self.feedback_history

    def is_won(self):
        """Возвращает True, если игрок угадал загаданное слово."""
        # Проверяем, была ли последняя попытка полностью правильной.
        if not self.feedback_history:
            return False

        last_feedback = self.feedback_history[-1]["feedback"]
        return all(status == "correct" for status in last_feedback)

    def attempts_left(self):
        """Возвращает количество попыток, оставшихся до конца игры."""
        # Количество оставшихся попыток = максимум минус уже сделанные попытки.
        return self.max_attempts - len(self.feedback_history)


if __name__ == "__main__":
    game = WordleGame("apple")

    # Первая попытка.
    print(game.guess("algae"))
    print(game.get_feedback())
    print(game.is_won())
    print(game.attempts_left())

    # Вторая попытка.
    print(game.guess("apple"))
    print(game.is_won())
    print(game.attempts_left())
