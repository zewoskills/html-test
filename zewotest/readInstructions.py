"""Пример чтения инструкций проекта из файла instructions.md."""

import logging
from pathlib import Path


logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def readInstructions(filePath: str) -> str:
    """Читает содержимое файла с инструкцией."""
    path = Path(filePath)

    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {filePath}")

    return path.read_text(encoding='utf-8')


def prepareRules(content: str) -> list[str]:
    """Возвращает список правил из Markdown-файла."""
    rules = []

    for line in content.splitlines():
        cleanedLine = line.strip()

        if cleanedLine.startswith('- '):
            rules.append(cleanedLine[2:].strip())

    return rules


def main() -> None:
    """Загружает инструкцию и выводит основные правила проекта."""
    filePath = Path(__file__).with_name('instructions.md')

    logging.info('Читаю инструкцию из файла: %s', filePath)
    content = readInstructions(str(filePath))
    rules = prepareRules(content)

    logging.info('Всего правил: %s', len(rules))
    for index, rule in enumerate(rules, start=1):
        logging.info('%s. %s', index, rule)


if __name__ == '__main__':
    main()
