"""
Микро-шаг 130: Импорт всех классов из модуля (Importing All Classes from a Module).
Синтаксис from module import * для импорта всех классов модуля.
В продакшн ML-коде этот подход не рекомендуется, но знание его нужно для
чтения чужого кода и понимания пространства имён (области доступных переменных).
"""

# Импорт ВСЕХ классов из модуля одной командой через звёздочку
from preprocessors import *

print("Импорт всех классов через 'from module import *':")

# Все классы модуля доступны напрямую, без указания имени модуля
# Это работает, но делает код непрозрачным: не видно, откуда взялись классы
scaler: StandardScaler = StandardScaler()
normalizer: MinMaxScaler = MinMaxScaler()
encoder: LabelEncoder = LabelEncoder()

print("\nСозданные предобработчики:")
scaler.describe()
normalizer.describe()
encoder.describe()

print("\nОбучение предобработчиков:")
scaler.fit()
normalizer.fit()
encoder.fit()

print("\nСостояние после обучения:")
scaler.describe()
normalizer.describe()
encoder.describe()