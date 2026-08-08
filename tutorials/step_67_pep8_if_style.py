"""
Микро-шаг 67: Стиль оформления if-выражений (PEP 8 for if Statements).
Правильное форматирование операторов сравнения в условных конструкциях.
В ML читаемость кода критична: код читают data scientists и инженеры,
а линтеры автоматически проверяют соответствие PEP 8.
"""

# Метрика качества модели (accuracy)
model_accuracy: float = 0.92

# Правильный стиль PEP 8: пробелы вокруг оператора сравнения
print("Проверка метрики модели (стиль PEP 8):")
if model_accuracy >= 0.95:
    print(f"  Accuracy {model_accuracy}: модель готова к продакшену")
elif model_accuracy >= 0.85:
    print(f"  Accuracy {model_accuracy}: модель требует доработки")
else:
    print(f"  Accuracy {model_accuracy}: модель не проходит базовый порог")

# Сравнение строк также оформляется с пробелами
model_status: str = "training"

print("\nПроверка статуса обучения:")
if model_status == "training":
    print("  Модель находится в процессе обучения")
elif model_status == "deployed":
    print("  Модель развёрнута в продакшене")
else:
    print("  Неизвестный статус модели")