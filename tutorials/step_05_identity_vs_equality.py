# src/step_05_identity_vs_equality.py
"""Разница между равенством (==) и идентичностью (is) в Python."""

# 1. Создаем два списка с абсолютно одинаковым содержимым
list_a: list[int] = [1, 2, 3]
list_b: list[int] = [1, 2, 3]

# 2. Сравниваем ЗНАЧЕНИЯ (Equality)
# Python смотрит внутрь списков и видит, что цифры совпадают.
print(f"list_a == list_b: {list_a == list_b}")

# 3. Сравниваем ИДЕНТИЧНОСТЬ (Identity)
# Оператор 'is' проверяет, ссылаются ли переменные на ОДИН И ТОТ ЖЕ объект в памяти.
print(f"list_a is list_b: {list_a is list_b}")

# 4. Проверяем через id() (это то же самое, что и 'is')
print(f"id(list_a) == id(list_b): {id(list_a) == id(list_b)}")

# 5. А теперь создаем третий список, просто присваивая ему первый
list_c: list[int] = list_a

# 6. Сравниваем list_a и list_c
print(f"list_a is list_c: {list_a is list_c}")