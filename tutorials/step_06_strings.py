# src/step_06_strings.py
"""Работа со строками и строковыми методами."""

# 1. Создание строк (можно использовать одинарные или двойные кавычки)
model_name: str = 'random forest'
dataset_path: str = "data/raw/wine_quality.csv"

# 2. Метод .title() — делает первую букву каждого слова заглавной
print(model_name.title())

# 3. Методы .upper() и .lower() — меняют регистр всех букв
print(model_name.upper())
print(model_name.lower())

# 4. f-strings (форматированные строки) — стандарт индустрии для вставки переменных в текст
# Мы используем их с самого дня 1, так как это читаемо и быстро (Matthes 2.2.2)
log_message: str = f"Model '{model_name.title()}' trained on {dataset_path}."
print(log_message)