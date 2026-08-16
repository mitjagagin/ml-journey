"""
Микро-шаг 59: Условные инструкции if-else (if-else Statements).
Конструкция if-else выполняет один из двух блоков в зависимости
от истинности условия. В ML это основа маршрутизации пайплайна:
деплой или переобучение, принятие предсказания или передача человеку.
"""

# Целевая точность для выхода в продакшен
target_accuracy: int = 95

# Сценарий 1: модель достигла цели
model_accuracy: int = 97

print("Сценарий 1: проверка готовности модели:")
if model_accuracy >= target_accuracy:
    print(f"  Точность {model_accuracy}% >= {target_accuracy}%")
    print("  Деплоим модель в продакшен")
else:
    print(f"  Точность {model_accuracy}% < {target_accuracy}%")
    print("  Отправляем модель на переобучение")

# Сценарий 2: модель не достигла цели
model_accuracy = 88

print("\nСценарий 2: проверка готовности модели:")
if model_accuracy >= target_accuracy:
    print(f"  Точность {model_accuracy}% >= {target_accuracy}%")
    print("  Деплоим модель в продакшен")
else:
    print(f"  Точность {model_accuracy}% < {target_accuracy}%")
    print("  Отправляем модель на переобучение")

# Human-in-the-loop: уверенное или неуверенное предсказание
confidence_threshold: float = 0.8
prediction_confidence: float = 0.72

print("\nПроверка уверенности предсказания:")
if prediction_confidence >= confidence_threshold:
    print(f"  Уверенность {prediction_confidence} >= {confidence_threshold}")
    print("  Предсказание принимается автоматически")
else:
    print(f"  Уверенность {prediction_confidence} < {confidence_threshold}")
    print("  Предсказание передаётся на проверку человеку")