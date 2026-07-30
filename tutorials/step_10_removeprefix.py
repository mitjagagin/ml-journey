# tutorials/step_10_removeprefix.py
"""Удаление префиксов из строк. Безопасная очистка путей и имен."""

# 1. Очистка пути к файлу (типичная задача Data Engineering)
file_path: str = "file:///data/raw/wine_quality.csv"
clean_path: str = file_path.removeprefix("file:///")
print(f"Original path: {file_path}")
print(f"Cleaned path:  {clean_path}")

# 2. Обработка имени модели или артефакта
model_name: str = "model_v2_random_forest"
short_name: str = model_name.removeprefix("model_v2_")
print(f"Short model name: {short_name}")

# 3. ВАЖНЫЙ нюанс: безопасность метода
# Если префикса нет, Python просто вернет исходную строку. Ошибки не будет!
# Это делает его гораздо безопаснее, чем ручные срезы (slicing).
safe_clean: str = file_path.removeprefix("http://")
print(f"Safe clean (prefix not found): {safe_clean}")