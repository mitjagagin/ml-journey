"""
Микро-шаг 147: Работа с несколькими файлами (Working with Multiple Files).
Обработка списка файлов одной функцией с перехватом ошибок.
В ML так можно обходить несколько файлов датасета (набора данных),
не останавливая пайплайн (последовательность шагов) из-за одного отсутствующего файла.
"""
from pathlib import Path


def count_words(filename: str):
    """Читает файл и печатает количество слов."""
    try:
        # Читаем весь файл как одну строку
        contents: str = Path(filename).read_text()

        # Разбиваем текст на список слов
        words: list[str] = contents.split()

        # Считаем количество слов
        num_words: int = len(words)

        print(f"В файле {filename} примерно {num_words} слов.")

    except FileNotFoundError:
        # Если файла нет, печатаем сообщение и продолжаем работу
        print(f"Файл {filename} не найден.")


# Список файлов для анализа
filenames: list[str] = [
    "model_report.txt",
    "ml_notes.txt",
    "missing_report.txt",
]

# Обрабатываем каждый файл по очереди
for filename in filenames:
    count_words(filename)