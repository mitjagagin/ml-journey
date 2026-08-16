"""
Микро-шаг 60: Цепочка if-elif-else (The if-elif-else Chain).
Конструкция if-elif-else проверяет несколько условий последовательно
и выполняет первый истинный блок. В ML это используется для
многоуровневой маршрутизации: выбор действия в зависимости от
значения метрики или статуса модели.
"""

# Целевые пороги для принятия решения о деплое
high_threshold: int = 95
medium_threshold: int = 90

# Фактическая точность модели
model_accuracy: int = 92

# Многоуровневая маршрутизация на основе accuracy
print("Решение о деплое на основе accuracy:")
if model_accuracy >= high_threshold:
    print(f"  Accuracy {model_accuracy}% >= {high_threshold}%")
    print("  Деплоим модель в продакшен")
elif model_accuracy >= medium_threshold:
    print(f"  Accuracy {model_accuracy}% >= {medium_threshold}%")
    print("  Отправляем на дообучение с тюнингом")
else:
    print(f"  Accuracy {model_accuracy}% < {medium_threshold}%")
    print("  Полный ретрейн модели")

# Второй сценарий: высокий accuracy
model_accuracy = 97

print("\nРешение о деплое (высокий accuracy):")
if model_accuracy >= high_threshold:
    print(f"  Accuracy {model_accuracy}% >= {high_threshold}%")
    print("  Деплоим модель в продакшен")
elif model_accuracy >= medium_threshold:
    print(f"  Accuracy {model_accuracy}% >= {medium_threshold}%")
    print("  Отправляем на дообучение с тюнингом")
else:
    print(f"  Accuracy {model_accuracy}% < {medium_threshold}%")
    print("  Полный ретрейн модели")

# Третий сценарий: низкий accuracy
model_accuracy = 85

print("\nРешение о деплое (низкий accuracy):")
if model_accuracy >= high_threshold:
    print(f"  Accuracy {model_accuracy}% >= {high_threshold}%")
    print("  Деплоим модель в продакшен")
elif model_accuracy >= medium_threshold:
    print(f"  Accuracy {model_accuracy}% >= {medium_threshold}%")
    print("  Отправляем на дообучение с тюнингом")
else:
    print(f"  Accuracy {model_accuracy}% < {medium_threshold}%")
    print("  Полный ретрейн модели")