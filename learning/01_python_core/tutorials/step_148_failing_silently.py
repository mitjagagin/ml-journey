"""
Микро-шаг 148: Молчаливая обработка ошибок (Failing Silently).
Использование оператора pass для игнорирования ошибки.
В ML pass используется в пайплайнах (последовательностях шагов),
когда отсутствие файла с датасетом (набором данных) - ожидаемая ситуация,
и не нужно засорять логи (журналы событий) сообщениями об ошибках.
"""
from pathlib import Path


def count_words(filename: str):
    """Читает файл и печатает количество слов.
    Если файла нет - молча пропускает его."""
    try:
        # Читаем весь файл как одну строку
        contents: str = Path(filename).read_text()

        # Разбиваем текст на список слов
        words: list[str] = contents.split()

        # Считаем количество слов
        num_words: int = len(words)

        print(f"В файле {filename} примерно {num_words} слов.")

    except FileNotFoundError:
        # pass говорит Python: "просто ничего не делай, продолжай дальше"
        pass


# Список файлов для анализа
filenames: list[str] = [
    "model_report.txt",
    "ml_notes.txt",
    "missing_report.txt",
]

# Обрабатываем каждый файл по очереди
for filename in filenames:
    count_words(filename)