"""
Микро-шаг 145: Анализ текста (Analyzing Text).
Чтение файла, разбиение текста на слова и подсчёт количества слов.
В ML так можно быстро оценить размер текстового датасета
(набора данных) перед более глубокой обработкой.
"""
from pathlib import Path

# Имя файла с текстом для анализа
filename: str = "model_report.txt"

try:
    # Читаем весь файл как одну строку
    contents: str = Path(filename).read_text()

    # Разбиваем текст на список слов
    words: list[str] = contents.split()

    # Считаем количество слов в списке
    num_words: int = len(words)

    print(f"В файле {filename} примерно {num_words} слов.")

except FileNotFoundError:
    # Этот блок выполнится, если файл не найден
    print(f"Файл {filename} не найден. Проверь имя файла и папку.")