'''
Микро-шаг 48: Стиль кода (Styling Your Code).
Основы PEP 8: именование переменных, отступы, длина строк, комментарии.
В ML чистый код критически важен для командной работы и поддержки
пайплайнов в продакшене.
'''

# Хорошее именование: snake_case, понятные имена
model_accuracy: float = 0.95
training_epochs: int = 10
batch_size: int = 32

print("Параметры модели:")
print(f"  Accuracy: {model_accuracy}")
print(f"  Epochs: {training_epochs}")
print(f"  Batch size: {batch_size}")

# Логические блоки разделены пустыми строками
# Комментарии объясняют "зачем", а не "что"

# Список метрик для мониторинга
metrics: list[str] = ['accuracy', 'precision', 'recall', 'f1_score']

print("\nМетрики для мониторинга:")
for metric in metrics:
    print(f"  {metric}")