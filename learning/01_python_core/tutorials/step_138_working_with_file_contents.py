"""
Микро-шаг 138: Работа с содержимым файла (Working with a File's Contents).
Чтение строк файла и сборка их в одну строку.
В ML так часто очищают сырые текстовые данные перед превращением
в признаки (отдельные свойства объекта).
"""

# Имя файла с числом pi
filename: str = "pi_digits.txt"

# Читаем файл и получаем список строк
with open(filename) as file_object:
    lines: list[str] = file_object.readlines()

# Создаём пустую строку, куда будем собирать чистые данные
pi_string: str = ""

# Проходим по каждой строке из файла
for line in lines:
    # strip() убирает пробелы и переносы строки по краям
    # += добавляет очищенную строку в конец pi_string
    pi_string += line.strip()

print("Собранное число pi:")
print(pi_string)

print(f"Длина строки: {len(pi_string)}")

print(f"Первые 10 символов: {pi_string[:10]}")