"""
Микро-шаг 76: Итерация по всем ключам словаря (Looping Through All the Keys).
Метод keys() возвращает только ключи словаря, без значений.
В ML это используется для получения списка всех признаков (колонок данных)
или всех параметров модели без их значений.
"""

# Признаки (колонки данных), используемые моделью
features: dict[str, str] = {
    'age': 'numerical',
    'income': 'numerical',
    'education': 'categorical',
    'city': 'categorical'
}

print("Все признаки модели:")
# Метод keys() возвращает только ключи
for feature in features.keys():
    print(f"  {feature}")

print("\nПараметры модели (только названия):")
hyperparameters: dict[str, int | float] = {
    'learning_rate': 0.01,
    'n_estimators': 100,
    'max_depth': 5
}

for param in hyperparameters.keys():
    print(f"  {param}")

# Проверка наличия конкретного признака
print("\nПроверка наличия признака:")
if 'age' in features.keys():
    print("  Признак 'age' есть в модели")

if 'social_security_number' in features.keys():
    print("  Признак 'social_security_number' есть в модели")
else:
    print("  Признак 'social_security_number' отсутствует")