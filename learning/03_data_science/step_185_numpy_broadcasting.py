"""
Микро-шаг 185: Векторизованные операции и Broadcasting (Vectorized Operations and Broadcasting).
Демонстрация поэлементных математических операций и механизма broadcasting в NumPy.
В ML это используется для масштабирования признаков (feature scaling) и добавления вектора смещения (bias) ко всем образцам сразу.
"""

import numpy as np


def main() -> None:
    # 1. Поэлементные операции (Element-wise operations)
    arr1: np.ndarray = np.array([1, 2, 3])
    arr2: np.ndarray = np.array([10, 20, 30])

    print("Поэлементное сложение:")
    print(f"  {arr1} + {arr2} = {arr1 + arr2}")

    # 2. Broadcasting: скаляр и массив
    # Скаляр автоматически "растягивается" до формы массива
    print("\nBroadcasting: умножение массива на скаляр (2):")
    print(f"  {arr1} * 2 = {arr1 * 2}")

    # 3. Broadcasting: 1D массив и 2D массив (матрица)
    matrix: np.ndarray = np.array([[1, 2, 3],
                                   [4, 5, 6]])
    bias: np.ndarray = np.array([10, 20, 30])  # Форма (3,)

    print("\nBroadcasting: сложение 2D матрицы и 1D вектора (bias):")
    print("Исходная матрица (форма 2x3):")
    print(matrix)
    print("Вектор смещения (bias, форма 3,):")
    print(bias)
    print("Результат сложения (bias добавляется к каждой строке матрицы):")
    print(matrix + bias)


if __name__ == "__main__":
    main()