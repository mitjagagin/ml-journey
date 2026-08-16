"""
Микро-шаг 146: Подсчёт вхождений слова (Counting Words).
Подсчёт, сколько раз слово встречается в тексте файла.
В ML это может быть простым признаком (отдельным свойством объекта)
при анализе текста.
"""
from pathlib import Path

# Имя файла с текстом для анализа
filename: str = "model_report.txt"

# Слово, которое хотим посчитать
target_word: str = "learning"

try:
    # Читаем весь файл как одну строку
    contents: str = Path(filename).read_text()

    # Переводим текст в нижний регистр, чтобы поиск не зависел от регистра
    text: str = contents.lower()

    # Считаем, сколько раз слово встречается в тексте
    word_count: int = text.count(target_word)

    print(f"Слово '{target_word}' встречается {word_count} раз(а).")

except FileNotFoundError:
    # Этот блок выполнится, если файл не найден
    print(f"Файл {filename} не найден. Проверь имя файла и папку.")