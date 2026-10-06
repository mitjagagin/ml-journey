"""
Микро-шаг 183: Многомерные массивы и срезы (Multidimensional Arrays and Slicing).
Создание 2D-массивов (матриц) и извлечение частей данных с помощью срезов.
В ML это используется для разделения данных на признаки (features) и целевые переменные (labels), а также для батчинга.
"""

import numpy as np


def main() -> None:
    # 1. Создание 2D-массива (матрицы) из списка списков
    data_list: list[list[int]] = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matrix: np.ndarray = np.array(data_list)

    print("Исходная матрица (2D массив):")
    print(matrix)
    print(f"Форма (shape): {matrix.shape}")  # (3, 3) -> 3 строки, 3 столбца

    # 2. Базовые срезы (Slicing)
    # Формат для 2D: matrix[строки, столбцы]

    # Взять вторую строку (индекс 1), все столбцы (:)
    second_row: np.ndarray = matrix[1, :]
    print("\nВторая строка (индекс 1):")
    print(f"  {second_row}")

    # Взять все строки (:), последний столбец (-1)
    last_column: np.ndarray = matrix[:, -1]
    print("\nПоследний столбец:")
    print(f"  {last_column}")

    # Взять подматрицу: первые две строки (0:2), первые два столбца (0:2)
    # Примечание: верхняя граница среза не включается
    submatrix: np.ndarray = matrix[0:2, 0:2]
    print("\nПодматрица (первые 2 строки и 2 столбца):")
    print(submatrix)


if __name__ == "__main__":
    main()