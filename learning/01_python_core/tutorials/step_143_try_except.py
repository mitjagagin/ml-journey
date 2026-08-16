"""
Микро-шаг 143: Использование try-except (Using try-except Blocks).
Обработка ошибки деления на ноль с помощью try-except.
В ML это помогает не падать при расчёте метрики
(числовой оценки качества модели), если данных для расчёта нет.
"""

# Числитель и знаменатель
numerator: int = 5
denominator: int = 0

# Блок try-except позволяет программе обработать ошибку, а не упасть
try:
    # Код, который может вызвать ошибку, помещаем внутрь try
    result: float = numerator / denominator
except ZeroDivisionError:
    # Этот блок выполняется, если возникла ошибка ZeroDivisionError
    print("Ошибка: делить на ноль нельзя.")