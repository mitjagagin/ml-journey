"""
Микро-шаг 128: Импорт нескольких классов из модуля (Importing Multiple Classes from a Module).
Импорт нескольких связанных классов из одного модуля для сборки ML-пайплайна.
В ML это позволяет импортировать все нужные метрики (числовые оценки качества)
одной строкой, делая код чище и короче.
"""

# Импорт ТРЁХ классов из модуля metrics одной строкой
from metrics import Accuracy, Precision, Recall

print("Оценка качества классификатора:")

# Создание экземпляров всех трёх метрик
accuracy_metric: Accuracy = Accuracy()
precision_metric: Precision = Precision()
recall_metric: Recall = Recall()

# Описание каждой метрики
accuracy_metric.describe()
precision_metric.describe()
recall_metric.describe()

# Пример вычислений
print("\nПример вычислений для бинарного классификатора:")

# Accuracy: 85 правильных из 100
acc_value: float = accuracy_metric.calculate(85, 100)
print(f"  Accuracy: {acc_value}")

# Precision: 70 истинно положительных, 10 ложно положительных
prec_value: float = precision_metric.calculate(70, 10)
print(f"  Precision: {prec_value}")

# Recall: 70 истинно положительных, 20 ложно отрицательных
rec_value: float = recall_metric.calculate(70, 20)
print(f"  Recall: {rec_value}")