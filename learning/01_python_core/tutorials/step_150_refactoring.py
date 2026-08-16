"""
Микро-шаг 150: Рефакторинг кода (Refactoring).
Разбиение большого блока кода на отдельные функции.
В ML-пайплайнах (последовательностях шагов) рефакторинг критически важен:
код разделяют на функции, чтобы его было легко поддерживать и тестировать.
"""
import json
from pathlib import Path


def get_stored_username(path: Path) -> str:
    """Возвращает сохранённое имя, если файл существует. Иначе возвращает пустую строку."""
    # Проверяем, существует ли файл на диске
    if path.exists():
        # Если существует, читаем его
        with open(path) as file_object:
            return json.load(file_object)

    # Если файла нет, возвращаем пустую строку
    return ""


def get_new_username(path: Path) -> str:
    """Запрашивает новое имя и сохраняет его в файл."""
    username: str = input("Как тебя зовут? ")

    with open(path, "w") as file_object:
        json.dump(username, file_object)

    return username


def greet_user(path: Path) -> None:
    """Главная функция: приветствует пользователя по имени."""
    # Пытаемся получить сохранённое имя
    username: str = get_stored_username(path)

    if username:
        # Если имя есть (строка не пустая), приветствуем
        print(f"С возвращением, {username}!")
    else:
        # Если имени нет, запрашиваем новое
        username = get_new_username(path)
        print(f"Мы запомним тебя, {username}!")


# Основная точка входа в программу
# Указываем путь к файлу, где будем хранить имя
path: Path = Path("username.json")

# Запускаем главную функцию
greet_user(path)