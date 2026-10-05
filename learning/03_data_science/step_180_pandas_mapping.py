"""
Микро-шаг 180: Трансформация и переименование данных (Mapping and Renaming).
Демонстрация применения функций к данным и изменения имен колонок.
В ML это основа feature engineering: создание новых признаков из существующих
и стандартизация имен для читаемости пайплайна.
"""

import pandas as pd


def demonstrate_mapping(df: pd.DataFrame) -> None:
    """Демонстрирует методы map, apply и rename."""
    print("1. Переименование колонок (rename):")
    # Передаем словарь, где ключ — старое имя, значение — новое
    df_renamed = df.rename(columns={"total_spent": "revenue", "is_premium": "premium_status"})
    print(f"   Новые колонки: {list(df_renamed.columns)}\n")

    print("2. Трансформация значений через map (для Series):")
    # lambda x: ... — это короткая анонимная функция без имени
    # Она принимает один аргумент (x) и возвращает результат выражения после ":"
    # .map() применяет эту функцию к КАЖДОМУ элементу колонки age
    age_groups = df['age'].map(lambda x: "Young" if x < 30 else "Adult")
    # .to_frame() превращает Series обратно в DataFrame для красивого вывода
    print(f"   Возрастные группы:\n{age_groups.to_frame().to_string(index=False)}\n")

    print("3. Трансформация значений через apply (для DataFrame или Series):")
    # .copy() создаёт полную независимую копию DataFrame
    # Это важно, чтобы изменения не повлияли на оригинальный df
    df_rounded = df.copy()

    # .apply() применяет функцию к КАЖДОМУ элементу колонки total_spent
    # lambda x: round(x) — округляет каждое число
    df_rounded['revenue_rounded'] = df_rounded['total_spent'].apply(lambda x: round(x))

    # Выводим только нужные колонки для наглядности
    print(f"   Данные с округленным доходом:\n{df_rounded[['user_id', 'total_spent', 'revenue_rounded']].to_string(index=False)}\n")


if __name__ == "__main__":
    raw_data = {
        "user_id": [1, 2, 3, 4, 5],
        "age": [25.0, 30.0, 35.0, 28.0, 22.0],
        "is_premium": [True, False, True, False, False],
        "total_spent": [150.50, 0.00, 320.75, 10.00, 12.00]
    }

    df = pd.DataFrame(raw_data)

    print("Демонстрация трансформации и переименования в Pandas:\n")
    demonstrate_mapping(df)