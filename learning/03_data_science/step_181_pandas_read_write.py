"""
Микро-шаг 181: Чтение и запись данных (Reading and Writing Data).
Демонстрация загрузки данных из CSV и сохранения DataFrame в CSV.
В ML это первый и последний шаг любого пайплайна: загрузка сырых данных
для анализа и сохранение очищенных признаков или предсказаний модели.
"""

import pandas as pd
from pathlib import Path


def demonstrate_io() -> None:
    """Демонстрирует сохранение и загрузку DataFrame."""
    # 1. Создаем тестовые данные
    raw_data = {
        "user_id": [1, 2, 3],
        "age": [25, 30, 35],
        "is_premium": [True, False, True]
    }
    df = pd.DataFrame(raw_data)

    # 2. Определяем путь к корню репозитория (3 уровня вверх от файла скрипта)
    # скрипт → 03_data_science → learning → корень
    repo_root = Path(__file__).resolve().parent.parent.parent
    data_dir = repo_root / "data" / "raw"
    data_dir.mkdir(parents=True, exist_ok=True)
    file_path = data_dir / "sample_users.csv"

    print("1. Сохранение DataFrame в CSV:")
    print(f"   Путь: {file_path}")
    # index=False критически важен! Иначе Pandas сохранит номера строк (0, 1, 2)
    # как отдельную безымянную колонку, что сломает загрузку в будущем.
    df.to_csv(file_path, index=False)
    print("   Файл успешно сохранен.\n")

    print("2. Чтение данных из CSV:")
    # Читаем файл обратно в новый DataFrame
    df_loaded = pd.read_csv(file_path)
    print(f"   Загруженные данные:\n{df_loaded.to_string(index=False)}\n")

    print("3. Проверка типов данных после загрузки:")
    # Pandas автоматически определяет типы данных при чтении
    print(df_loaded.dtypes)


if __name__ == "__main__":
    demonstrate_io()