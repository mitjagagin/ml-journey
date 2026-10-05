"""
Микро-шаг 179: Работа с пропущенными значениями (Missing Values).
Демонстрация обнаружения и обработки пропусков (NaN/None) в DataFrame.
В ML это обязательный этап предобработки: модели не могут обучаться на пропусках,
поэтому их нужно либо удалить, либо заполнить (импутировать) осмысленными значениями.
"""

import pandas as pd


def handle_missing_values(df: pd.DataFrame) -> None:
    """Демонстрирует основные стратегии работы с пропущенными значениями."""
    print("1. Обнаружение пропусков (сколько пропусков в каждой колонке):")
    # isna() возвращает DataFrame из True/False, sum() суммирует True как 1
    missing_counts = df.isna().sum()
    print(f"   {missing_counts}\n")

    print("2. Стратегия А: Удаление строк с пропусками (dropna):")
    # Полезно, если пропусков мало, а данных много
    df_dropped = df.dropna(subset=['age'])
    print(f"   Размер после удаления: {df_dropped.shape}")
    print(f"   Данные:\n{df_dropped.to_string(index=False)}\n")

    print("3. Стратегия Б: Заполнение пропусков (fillna):")
    # Полезно, чтобы не терять строки. Заполняем средним возрастом или константой
    median_age = df['age'].median()
    df_filled = df.copy()  # Создаем копию, чтобы не менять оригинал
    df_filled['age'] = df_filled['age'].fillna(median_age)
    print(f"   Медианный возраст для заполнения: {median_age}")
    print(f"   Данные после заполнения:\n{df_filled.to_string(index=False)}\n")


if __name__ == "__main__":
    raw_data = {
        "user_id": [1, 2, 3, 4, 5],
        "age": [25.0, 30.0, None, 28.0, 22.0],  # Один пропуск
        "is_premium": [True, False, True, False, None],  # Еще один пропуск
        "total_spent": [150.50, 0.00, 320.75, 10.00, 12.00]
    }

    df = pd.DataFrame(raw_data)

    print("Демонстрация работы с пропущенными значениями в Pandas:\n")
    handle_missing_values(df)