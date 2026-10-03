"""
Микро-шаг 176: Введение в Pandas (Introduction to Pandas).
Создание DataFrame и базовый осмотр табличных данных.
В ML это первый шаг после загрузки датасета: мы должны понять его размер,
типы данных и увидеть первые строки перед любым анализом или очисткой.
"""

import pandas as pd


def inspect_dataframe(df: pd.DataFrame) -> None:
    """Выводит базовую информацию о DataFrame для первичного анализа."""
    print("1. Размер данных (строки, колонки):")
    print(f"   {df.shape}\n")

    print("2. Первые 3 строки данных:")
    # Используем head(3), чтобы не засорять консоль, если данных много
    print(f"   {df.head(3).to_string(index=False)}\n")

    print("3. Информация о типах данных и пропусках:")
    # info() выводит сводку: количество не-Null значений и тип данных (dtype)
    df.info()
    print("-" * 40)


if __name__ == "__main__":
    # Имитация загрузки небольшого табличного датасета из словаря
    # В реальности мы будем использовать pd.read_csv("path/to/data.csv")
    raw_data = {
        "user_id": [1, 2, 3, 4, 5],
        "age": [25, 30, 35, None, 22],  # None имитирует пропущенное значение (NaN)
        "is_premium": [True, False, True, True, False],
        "total_spent": [150.50, 0.00, 320.75, 89.90, 12.00]
    }

    # Создание объекта DataFrame
    df = pd.DataFrame(raw_data)

    print("Начало первичного осмотра датасета:\n")
    inspect_dataframe(df)