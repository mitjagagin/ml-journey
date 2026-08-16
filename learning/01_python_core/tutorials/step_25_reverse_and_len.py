"""
Микро-шаг 25: Обратный порядок и длина списка.
- len(список) возвращает количество элементов (критично для проверки размера данных).
- .reverse() меняет порядок элементов в списке навсегда (in-place).
"""

# Список этапов ML-пайплайна в хронологическом порядке
pipeline_steps: list[str] = ["Data Collection", "Feature Engineering", "Model Training", "Evaluation", "Deployment"]

# 1. Определяем длину списка
num_steps: int = len(pipeline_steps)
print(f"Всего этапов в пайплайне: {num_steps}")
print(f"Исходный порядок: {pipeline_steps}")

# 2. Меняем порядок на обратный (например, чтобы начать разбор с конца)
pipeline_steps.reverse()
print(f"Обратный порядок (после .reverse()): {pipeline_steps}")