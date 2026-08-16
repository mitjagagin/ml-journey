"""
Микро-шаг 106: Защита списка от изменений (Preventing a Function from Modifying a List).
Передача копии списка через срез [:], чтобы оригинал остался нетронутым.
В ML это нужно, когда оригинальные данные нужны для повторных экспериментов
или сравнения результатов до и после обработки.
"""

# Та же функция, что и в шаге 105
def process_samples(raw_samples: list[str], processed_samples: list[str]) -> None:
    while raw_samples:
        sample: str = raw_samples.pop()
        processed_samples.append(sample)

# Исходные данные
raw_data: list[str] = ["sample_001", "sample_002", "sample_003"]
processed_data: list[str] = []

# Передаём КОПИЮ raw_data через срез [:]
# processed_data передаём напрямую — он МОЖЕТ изменяться
print("До обработки:")
print(f"  Необработанные: {raw_data}")
print(f"  Обработанные: {processed_data}")

print("\nПроцесс обработки:")
process_samples(raw_data[:], processed_data)

# raw_data НЕ изменился, потому что мы передали копию
print("\nПосле обработки:")
print(f"  Необработанные (оригинал): {raw_data}")
print(f"  Обработанные: {processed_data}")