"""
Микро-шаг 65: Проверка, что список не пустой (Checking That a List Is Not Empty).
Проверка if list_name: использует истинность списка:
пустой список даёт False, непустой — True.
В ML это используется для валидации данных перед обработкой:
проверка датасета, батча или списка результатов перед использованием.
"""

# Сценарий 1: список с данными для обработки
training_data: list[str] = ["sample_1", "sample_2", "sample_3"]

print("Проверка непустого списка данных:")
if training_data:
    print("  Список не пуст, запускаем обработку")
    for sample in training_data:
        print(f"    Обработка: {sample}")
else:
    print("  Список пуст, обработка не требуется")

# Сценарий 2: пустой список ошибок предсказания
failed_predictions: list[str] = []

print("\nПроверка пустого списка ошибок:")
if failed_predictions:
    print("  Есть ошибки предсказаний, запускаем анализ")
    for prediction in failed_predictions:
        print(f"    Анализ: {prediction}")
else:
    print("  Ошибок нет, анализ не требуется")