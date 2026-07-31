# tutorials/step_12_numbers_and_comments.py
"""Работа с числами (int, float) и профессиональные комментарии."""

# 1. Целые числа (Integers)
batch_size: int = 32
num_epochs: int = 10

# 2. Числа с плавающей точкой (Floats)
learning_rate: float = 0.001
accuracy: float = 0.95

# 3. Базовая арифметика
total_steps: int = batch_size * num_epochs
print(f"Total training steps: {total_steps}")

# 4. ВАЖНО: Деление в Python
# Обычное деление (/) ВСЕГДА возвращает float, даже если числа делятся нацело
normal_division: float = 10 / 2
print(f"10 / 2 = {normal_division} (type: {type(normal_division).__name__})")

# Целочисленное деление (//) возвращает int (отбрасывает дробную часть)
# Полезно для расчета индексов или разбиения данных на фолды
integer_division: int = 10 // 3
print(f"10 // 3 = {integer_division} (type: {type(integer_division).__name__})")

# 5. Комментарии
# Плохой комментарий (описывает очевидное):
# x = 5 # присваиваем 5 иксу

# Хороший комментарий (объясняет "почему" или бизнес-логику):
# Используем 0.95 как порог отсечения, так как по требованию бизнеса
# мы готовы жертвовать полнотой (recall) ради высокой точности (precision).
confidence_threshold: float = 0.95