"""
Микро-шаг 91: Перемещение элементов между списками (Moving Items from One List to Another).
Цикл while с pop() позволяет извлекать элементы из одного списка
и добавлять их в другой, пока исходный список не опустеет.
В ML это используется в пайплайнах (последовательностях шагов
обработки данных): например, брать необработанные примеры из очереди
и после валидации (проверки качества) перемещать в список готовых
для обучения модели.
"""

# Список датасетов (наборов данных), которые нужно проверить
unverified_datasets: list[str] = ["titanic", "housing", "wine", "iris"]

# Пустой список для уже проверенных датасетов
verified_datasets: list[str] = []

print("Начало процесса валидации датасетов:")
print(f"  Непроверенных: {len(unverified_datasets)}")
print(f"  Проверенных: {len(verified_datasets)}\n")

# Цикл работает, пока в списке есть элементы
# while unverified_datasets — это сокращение от while len(unverified_datasets) > 0
while unverified_datasets:
    # Извлекаем ПОСЛЕДНИЙ элемент из списка
    current_dataset: str = unverified_datasets.pop()
    print(f"Проверяем датасет: {current_dataset}")

    # Добавляем его в список проверенных
    verified_datasets.append(current_dataset)

print("\nВалидация завершена!")
print(f"  Непроверенных осталось: {len(unverified_datasets)}")
print(f"  Проверенных: {len(verified_datasets)}")

# Выводим все проверенные датасеты
print("\nСписок готовых к обучению датасетов:")
for dataset in verified_datasets:
    print(f"  {dataset}")