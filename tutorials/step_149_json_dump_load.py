"""
Микро-шаг 149: Сохранение и чтение JSON (Using json.dump and json.load).
Сохранение данных Python в файл формата JSON и их обратное чтение.
В ML формат JSON — это стандарт для сохранения конфигов
(файлов с настройками модели) и обмена данными.
"""
import json
from pathlib import Path

# Список чисел, который мы хотим сохранить
numbers: list[int] = [2, 3, 5, 7, 11, 13]

# Путь к файлу
path: Path = Path("numbers.json")

# 1. Сохраняем список в файл
# Открываем файл в режиме записи ('w'), который мы изучили в шаге 139
with open(path, "w") as file_object:
    # json.dump() берёт данные Python и записывает их в открытый файл
    json.dump(numbers, file_object)

# 2. Читаем список обратно из файла
# Открываем файл для чтения (режим по умолчанию)
with open(path) as file_object:
    # json.load() читает данные из открытого файла и возвращает объект Python
    loaded_numbers: list[int] = json.load(file_object)

print("Загруженные из файла числа:")
print(loaded_numbers)