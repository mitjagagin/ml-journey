"""
Микро-шаг 139: Запись в файл (Writing to a File).
Запись одной строки в файл в режиме 'w'.
В ML запись в файл нужна, чтобы сохранять конфиги (файлы с настройками)
и логи (журналы событий).
"""

# Имя файла для записи
filename: str = "programming.txt"

# Открываем файл в режиме 'w' (write - запись).
# Если файла нет, он будет создан.
# Если файл уже есть, его старое содержимое будет удалено.
with open(filename, "w") as file_object:
    # Записываем одну строку в файл
    file_object.write("I love programming.")

# Проверяем результат: читаем файл и печатаем содержимое
with open(filename) as file_object:
    contents: str = file_object.read()

print("Содержимое файла после записи:")
print(contents)