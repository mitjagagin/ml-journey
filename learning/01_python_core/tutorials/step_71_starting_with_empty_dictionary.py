"""
Микро-шаг 71: Начало с пустого словаря (Starting with an Empty Dictionary).
Создание пустого словаря и последующее добавление пар ключ-значение.
В ML это используется для сбора метрик по ходу эксперимента,
накопления результатов обработки данных и динамического построения маппингов.
"""

# Начинаем с пустого словаря для метрик эксперимента
experiment_metrics: dict[str, float] = {}

print("Метрики до начала обучения:")
print(f"  {experiment_metrics}")

# Добавляем метрики по ходу эксперимента
experiment_metrics['train_loss'] = 0.95
experiment_metrics['val_loss'] = 0.92
experiment_metrics['train_accuracy'] = 0.72

print("\nМетрики после первой эпохи:")
print(f"  {experiment_metrics}")

# Другой пример: строим маппинг категорий (label encoding)
category_mapping: dict[str, int] = {}

# Добавляем категории по мере их встречи в данных
category_mapping['cat'] = 0
category_mapping['dog'] = 1
category_mapping['bird'] = 2

print("\nМаппинг категорий для модели:")
print(f"  {category_mapping}")

# Проверяем, что конкретная категория закодирована правильно
print("\nПроверка кодировки:")
print(f"  Категория 'dog' закодирована как: {category_mapping['dog']}")