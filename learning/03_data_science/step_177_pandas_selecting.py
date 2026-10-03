"""
Микро-шаг 177: Выбор данных в Pandas (Indexing, Selecting & Filtering).
Демонстрация выбора конкретных колонок (признаков) и фильтрации строк.
В ML это основа feature selection (отбора признаков) и фильтрации датасета
(например, удаление выбросов или выбор конкретного класса для обучения).
"""

import pandas as pd


def demonstrate_selection(df: pd.DataFrame) -> None:
    """Демонстрирует различные способы выбора данных в DataFrame."""
    print("1. Выбор одной колонки (возвращает объект Series):")
    print(f"   Тип объекта: {type(df['age'])}")
    print(f"   Данные:\n{df['age']}\n")

    print("2. Выбор нескольких колонок (возвращает DataFrame):")
    # Обратите внимание на двойные квадратные скобки: внешние для списка, внутренние для синтаксиса Pandas
    subset = df[['user_id', 'total_spent']]
    print(f"   Тип объекта: {type(subset)}")
    print(f"   Данные:\n{subset.to_string(index=False)}\n")

    print("3. Фильтрация строк по условию (Boolean Indexing):")
    # Создаем маску (Series из True/False) и применяем её к DataFrame
    premium_mask = df['is_premium'] == True
    premium_users = df[premium_mask]
    print(f"   Премиум пользователи:\n{premium_users.to_string(index=False)}\n")

    print("4. Комбинированная фильтрация (несколько условий):")
    # Используем побитовые операторы & (AND) и | (OR). Условия обязательно в скобках!
    active_premium = df[(df['is_premium'] == True) & (df['total_spent'] > 50.0)]
    print(f"   Активные премиум пользователи (потратили > 50):\n{active_premium.to_string(index=False)}\n")


if __name__ == "__main__":
    raw_data = {
        "user_id": [1, 2, 3, 4, 5],
        "age": [25.0, 30.0, 35.0, None, 22.0],
        "is_premium": [True, False, True, True, False],
        "total_spent": [150.50, 0.00, 320.75, 89.90, 12.00]
    }

    df = pd.DataFrame(raw_data)

    print("Демонстрация выбора данных в Pandas:\n")
    demonstrate_selection(df)