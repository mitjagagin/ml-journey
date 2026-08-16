"""
Микро-шаг 105: Изменение списка в функции (Modifying a List in a Function).
Функция изменяет переданный список, и изменения сохраняются после вызова.
В ML это используется при предобработке данных: функция перемещает или
изменяет элементы, и результат остаётся в исходном списке.
"""

# Функция перемещает элементы из raw_samples в processed_samples
def process_samples(raw_samples: list[str], processed_samples: list[str]) -> None:
    while raw_samples:
        sample: str = raw_samples.pop()
        print(f"  Обработка образца: {sample}")
        processed_samples.append(sample)

# Исходные данные
raw_data: list[str] = ["sample_001", "sample_002", "sample_003"]
processed_data: list[str] = []

print("До обработки:")
print(f"  Необработанные: {raw_data}")
print(f"  Обработанные: {processed_data}")

# Передаём оба списка в функцию — они ИЗМЕНЯЮТСЯ внутри
print("\nПроцесс обработки:")
process_samples(raw_data, processed_data)

# После вызова функции изменения СОХРАНИЛИСЬ
print("\nПосле обработки:")
print(f"  Необработанные: {raw_data}")
print(f"  Обработанные: {processed_data}")