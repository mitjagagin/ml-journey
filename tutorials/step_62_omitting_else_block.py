"""
Микро-шаг 62: Пропуск блока else (Omitting the else Block).
Блок else не обязателен — можно писать только явные условия.
В ML это применяется для обработки только известных значений:
если значение не в списке допустимых, код просто ничего не делает.
"""

# Известные статусы модели в системе
known_statuses: list[str] = ["ready", "training", "failed", "testing"]

# Статус, который пришёл из мониторинга
current_status: str = "ready"

# Обработка только известных статусов (без else)
print("Обработка статуса модели:")
if current_status == "ready":
    print(f"  Статус '{current_status}': модель готова к инференсу")
elif current_status == "training":
    print(f"  Статус '{current_status}': модель обучается")
elif current_status == "failed":
    print(f"  Статус '{current_status}': требуется переобучение")
elif current_status == "testing":
    print(f"  Статус '{current_status}': модель на A/B тестировании")
# Если статус неизвестный — ничего не делаем (нет else блока)

# Неизвестный статус
unknown_status: str = "deprecated"

print("\nОбработка неизвестного статуса:")
if unknown_status == "ready":
    print(f"  Статус '{unknown_status}': модель готова к инференсу")
elif unknown_status == "training":
    print(f"  Статус '{unknown_status}': модель обучается")
elif unknown_status == "failed":
    print(f"  Статус '{unknown_status}': требуется переобучение")
elif unknown_status == "testing":
    print(f"  Статус '{unknown_status}': модель на A/B тестировании")
# Никакого вывода — код просто пропускает неизвестный статус

# Пример с числовыми условиями (без else)
accuracy_threshold: int = 90
model_accuracy: int = 85

print("\nПроверка accuracy (только если выше порога):")
if model_accuracy >= accuracy_threshold:
    print(f"  Accuracy {model_accuracy}% >= {accuracy_threshold}%: модель готова")
# Если accuracy ниже порога — ничего не делаем