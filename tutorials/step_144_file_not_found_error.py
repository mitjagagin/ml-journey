"""
Микро-шаг 144: Обработка ошибки отсутствия файла (FileNotFoundError).
Перехват ошибки, если файл не найден.
В ML так можно обработать ситуацию, когда датасет (набор данных)
ещё не загружен или путь к нему указан неверно.
"""
from pathlib import Path

# Имя файла, которого нет в папке tutorials
filename: str = "missing_file.txt"

# Пробуем прочитать файл
try:
    contents: str = Path(filename).read_text()
except FileNotFoundError:
    # Этот блок выполняется, если файла не существует
    print(f"Файл {filename} не найден. Проверь имя файла и папку.")