"""
Микро-шаг 186: Матричное умножение и линейная алгебра (NumPy Linear Algebra and Dot Product).
Демонстрация скалярного и матричного умножения с проверкой совместимости размерностей.
В ML это используется для вычисления предсказаний модели (умножение матрицы признаков на вектор весов).
"""

import numpy as np


def main() -> None:
    # 1. Скалярное произведение двух 1D-векторов (Dot Product)
    features: np.ndarray = np.array([2.0, 3.0, 1.0])  # Признаки объекта
    weights: np.ndarray = np.array([0.5, 1.0, -0.5])  # Веса модели

    # Вычисляем скалярное произведение: (2*0.5) + (3*1.0) + (1*-0.5) = 1.0 + 3.0 - 0.5 = 3.5
    prediction_1d: float = np.dot(features, weights)

    print("Скалярное произведение (1D векторы):")
    print(f"  Результат: {prediction_1d}")

    # 2. Матричное умножение (2D массив на 1D вектор или 2D на 2D)
    # Представим, что у нас 2 объекта (строки) и 3 признака (столбцы)
    batch_features: np.ndarray = np.array([
        [2.0, 3.0, 1.0],  # Объект 1
        [1.0, 0.0, 4.0]  # Объект 2
    ])

    # Используем оператор @ (современный аналог np.dot для матриц в Python 3.5+)
    predictions_2d: np.ndarray = batch_features @ weights

    print("\nМатричное умножение (2D матрица на 1D вектор весов):")
    print("  Предсказания для двух объектов:")
    print(f"  {predictions_2d}")

    # 3. Проверка несовместимости размерностей (закомментировано, чтобы скрипт не падал)
    # wrong_weights: np.ndarray = np.array([0.5, 1.0])  # Только 2 веса вместо 3
    # Ошибка: ValueError: matmul: Input operand 1 has a mismatch in its core dimension...
    # print(batch_features @ wrong_weights)


if __name__ == "__main__":
    main()