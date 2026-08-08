"""
Микро-шаг 53: Числовые сравнения (Numerical Comparisons).
Операторы больше >, меньше <, больше или равно >=, меньше или равно <=.
В ML числовые сравнения управляют обучением: остановка при достижении
нужного значения loss, порог уверенности модели, контроль точности.
"""

# Целевое значение accuracy для выхода модели в продакшен
target_accuracy: int = 95

# Фактическая accuracy после обучения
model_accuracy: int = 92

# Проверка: готова ли модель к продакшену
print("Проверка готовности модели:")
if model_accuracy >= target_accuracy:
    print(f"  Модель готова: {model_accuracy} >= {target_accuracy}")
else:
    print(f"  Модель не готова: {model_accuracy} < {target_accuracy}")

# Порог уверенности для принятия предсказания
confidence_threshold: int = 80
prediction_confidence: int = 87

print("\nПроверка уверенности предсказания:")
if prediction_confidence > confidence_threshold:
    print(f"  Предсказание принимается: {prediction_confidence} > {confidence_threshold}")
else:
    print("  Предсказание отклонено, уверенность слишком низкая")

# Ранняя остановка обучения: loss упал ниже цели
target_loss: float = 0.1
current_loss: float = 0.08

print("\nПроверка ранней остановки обучения:")
if current_loss <= target_loss:
    print(f"  Обучение останавливаем: loss {current_loss} <= {target_loss}")
else:
    print("  Продолжаем обучение")