"""
Микро-шаг 127: Хранение нескольких классов в одном модуле (Storing Multiple Classes in a Module).
Хранение связанных классов в одном модуле и разные способы их импорта.
В ML это позволяет группировать логически связанные классы (например, датасет и предобработчик)
в одном файле, упрощая структуру проекта и импорты.
"""

# СПОСОБ 1: Импорт одного класса из модуля с несколькими классами
from dataset import Dataset

print("Способ 1: Импорт одного класса:")
iris: Dataset = Dataset("Iris", 150)
iris.describe()

# СПОСОБ 2: Импорт нескольких классов через запятую
from dataset import Dataset, Preprocessor

print("\nСпособ 2: Импорт нескольких классов:")
wine: Dataset = Dataset("Wine", 178)
scaler: Preprocessor = Preprocessor("StandardScaler")
wine.describe()
scaler.fit()
scaler.describe()

# СПОСОБ 3: Импорт всего модуля (обращение через точку)
import dataset

print("\nСпособ 3: Импорт всего модуля:")
housing: dataset.Dataset = dataset.Dataset("Housing", 20640)
normalizer: dataset.Preprocessor = dataset.Preprocessor("MinMaxScaler")
housing.describe()
normalizer.fit()
normalizer.describe()