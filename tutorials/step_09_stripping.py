# tutorials/step_09_stripping.py
"""Удаление пробелов из строк. Критично для очистки данных (Data Cleaning)."""

# Создаем строку с лишними пробелами и табуляцией по краям
raw_data: str = "   \t random_forest_model \t   "

# 1. .rstrip() — удаляет пробелы СПРАВА (right)
print(f"rstrip: '{raw_data.rstrip()}'")

# 2. .lstrip() — удаляет пробелы СЛЕВА (left)
print(f"lstrip: '{raw_data.lstrip()}'")

# 3. .strip() — удаляет пробелы С ОБЕИХ СТОРОН (самый частый метод)
clean_data: str = raw_data.strip()
print(f"strip: '{clean_data}'")