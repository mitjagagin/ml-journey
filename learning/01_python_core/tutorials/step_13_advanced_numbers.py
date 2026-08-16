# tutorials/step_13_advanced_numbers.py
"""Продвинутые фишки чисел: подчеркивания, множественное присваивание, константы."""

# 1. Подчеркивания в числах (Underscores in Numbers)
# Python игнорирует подчеркивания, но они делают большие числа читаемыми.
num_rows: int = 1_500_000
num_parameters: int = 7_000_000_000
print(f"Dataset size: {num_rows} rows")
print(f"Model parameters: {num_parameters}")

# 2. Множественное присваивание (Multiple Assignment)
# Позволяет присвоить значения нескольким переменным в одной строке.
# Очень полезно при распаковке метрик модели.
accuracy, precision, recall = 0.95, 0.92, 0.89
print(f"Metrics -> Acc: {accuracy}, Prec: {precision}, Rec: {recall}")

# 3. Константы (Constants)
# В Python нет встроенной защиты констант, но по стандарту PEP 8
# их принято называть ЗАГЛАВНЫМИ БУКВАМИ. Это сигнал для разработчиков:
# "Не меняй это значение в коде!" (обычно это гиперпараметры или пути).
MAX_EPOCHS: int = 100
LEARNING_RATE: float = 0.001
DATA_PATH: str = "data/raw/"

print(f"Training for {MAX_EPOCHS} epochs with LR={LEARNING_RATE}")