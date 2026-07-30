# src/step_03_name_error.py
"""Демонстрация NameError и чтение traceback."""

# 1. Создаём переменную в нижнем регистре
message = "Hello Python world!"

# 2. Выводим её (всё верно)
print(message)

# 3. Намеренно делаем опечатку: пишем 'Message' с большой буквы
# Python не знает такую переменную!
print(Message)