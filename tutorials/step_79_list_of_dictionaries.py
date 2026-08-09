"""
Микро-шаг 79: Список словарей (A List of Dictionaries).
Список, в котором каждый элемент является словарем.
В ML так часто представляют датасет: каждая строка — словарь признаков,
где ключи — названия колонок, а значения — данные.
"""

# Датасет: три образца данных с признаками (колонками)
dataset: list[dict[str, float]] = [
    {'age': 25.0, 'income': 50000.0, 'credit_score': 720.0},
    {'age': 30.0, 'income': 60000.0, 'credit_score': 680.0},
    {'age': 35.0, 'income': 75000.0, 'credit_score': 750.0}
]

print("Весь датасет:")
print(f"  {dataset}")

print("\nДоступ к первому образцу данных:")
first_sample: dict[str, float] = dataset[0]
print(f"  {first_sample}")

print("\nДоступ к конкретному признаку первого образца:")
first_age: float = dataset[0]['age']
print(f"  Возраст первого образца: {first_age}")

print("\nПеребор всех образцов датасета:")
for sample in dataset:
    print(f"  Возраст: {sample['age']}, Доход: {sample['income']}")

# Добавляем новый образец данных в датасет
new_sample: dict[str, float] = {'age': 40.0, 'income': 90000.0, 'credit_score': 800.0}
dataset.append(new_sample)

print("\nДатасет после добавления нового образца:")
for sample in dataset:
    print(f"  Возраст: {sample['age']}, Доход: {sample['income']}, Кредитный рейтинг: {sample['credit_score']}")