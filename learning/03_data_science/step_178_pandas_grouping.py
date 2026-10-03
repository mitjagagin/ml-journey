"""
Микро-шаг 178: Группировка и сортировка данных (Grouping and Sorting).
Демонстрация агрегации данных по категориям и сортировки результатов.
В ML это основа feature engineering: создание агрегированных признаков
(например, средний чек по категории пользователя) перед обучением модели.
"""

import pandas as pd


def demonstrate_grouping(df: pd.DataFrame) -> None:
    """Демонстрирует группировку и сортировку данных."""
    print("1. Группировка по одной колонке с агрегацией (среднее значение):")
    # Группируем по is_premium и считаем среднее по total_spent
    avg_spent = df.groupby('is_premium')['total_spent'].mean()
    print(f"   {avg_spent}\n")

    print("2. Множественная агрегация (несколько статистик сразу):")
    # Используем agg() для получения минимума, максимума и среднего
    stats = df.groupby('is_premium')['total_spent'].agg(['min', 'max', 'mean'])
    print(f"   {stats}\n")

    print("3. Сортировка результатов по убыванию:")
    # Сортируем по среднему чеку, чтобы увидеть самую прибыльную группу первой
    sorted_stats = stats.sort_values(by='mean', ascending=False)
    print(f"   {sorted_stats}\n")


if __name__ == "__main__":
    raw_data = {
        "user_id": [1, 2, 3, 4, 5, 6],
        "age": [25.0, 30.0, 35.0, 28.0, 22.0, 40.0],
        "is_premium": [True, False, True, False, False, True],
        "total_spent": [150.50, 0.00, 320.75, 10.00, 12.00, 500.00]
    }

    df = pd.DataFrame(raw_data)

    print("Демонстрация группировки и сортировки в Pandas:\n")
    demonstrate_grouping(df)