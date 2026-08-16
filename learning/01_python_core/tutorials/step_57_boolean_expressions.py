"""
Микро-шаг 57: Булевы выражения (Boolean Expressions).
Сохранение результата сравнения (True/False) в переменную.
В ML boolean-флаги управляют потоком выполнения пайплайна:
is_ready для деплоя, has_error для отката, is_validated для продолжения.
"""

# Целевые метрики для выхода модели в продакшен
target_accuracy: int = 95
target_latency: int = 100

# Фактические показатели модели
model_accuracy: int = 92
model_latency: int = 80

# Сохраняем результат проверки в boolean-флаг
is_accurate_enough: bool = model_accuracy >= target_accuracy
is_fast_enough: bool = model_latency <= target_latency

print("Boolean-флаги для модели:")
print(f"  is_accurate_enough: {is_accurate_enough}")
print(f"  is_fast_enough: {is_fast_enough}")

# Комбинируем флаги через and
is_ready: bool = is_accurate_enough and is_fast_enough

print(f"\nФлаг готовности к деплою:")
print(f"  is_ready: {is_ready}")

# Используем флаг в условии
print("\nРешение о деплое:")
if is_ready:
    print("  Деплоим модель в продакшен")
else:
    print("  Модель требует доработки")

# Проверяем наличие ошибки (симуляция)
has_error: bool = False

print("\nПроверка на ошибки:")
if has_error:
    print("  Обнаружена ошибка, откатываем изменения")
else:
    print("  Ошибок нет, продолжаем работу")