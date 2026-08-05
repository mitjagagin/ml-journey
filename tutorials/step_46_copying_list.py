'''
Микро-шаг 46: Копирование списка (Copying a List).
Создание независимой копии списка с помощью среза [:].
В ML это критически важно для создания независимых копий батчей данных,
чтобы трансформации (аугментации, нормализация) не изменяли
исходные "сырые" данные.
'''

# Датасет: список признаков (features)
raw_features: list[str] = ['age', 'salary', 'city']

# Правильное копирование: срез [:] создаёт НОВЫЙ список в памяти
processed_features: list[str] = raw_features[:]
processed_features.append('normalized_salary')

print("Сырые данные (raw):")
print(f"  {raw_features}")

print("\nОбработанные данные (processed):")
print(f"  {processed_features}")

# Неправильное копирование: присваивание = ссылка на тот же объект
original_batch: list[str] = ['image_1.jpg', 'image_2.jpg']

# Здесь мы НЕ создаём новый список, а даём второе имя тому же объекту
augmented_batch: list[str] = original_batch
augmented_batch.append('image_3.jpg')

print("\nОригинал (неправильное копирование через =):")
print(f"  {original_batch}")

print("\nКопия (неправильное копирование через =):")
print(f"  {augmented_batch}")