"""
Микро-шаг 182: Введение в NumPy и создание массивов (NumPy Basics and ndarray Creation).
Создание базовых массивов NumPy из списков Python и проверка их атрибутов.
В ML это используется как фундамент для представления признаков (features) в виде матриц для обучения моделей.
"""

import numpy as np


def main() -> None:
    # 1. Создание массива из списка Python
    python_list: list[int] = [1, 2, 3, 4, 5]
    numpy_array: np.ndarray = np.array(python_list)

    print("Исходный список Python:")
    print(f"  Значение: {python_list}")
    print(f"  Тип: {type(python_list)}")

    print("\nМассив NumPy (ndarray):")
    print(f"  Значение: {numpy_array}")
    print(f"  Тип: {type(numpy_array)}")

    # 2. Проверка ключевых атрибутов ndarray
    print("\nАтрибуты массива NumPy:")
    print(f"  Форма (shape): {numpy_array.shape}")
    print(f"  Тип данных (dtype): {numpy_array.dtype}")
    print(f"  Размерность (ndim): {numpy_array.ndim}")

    # 3. Демонстрация векторизации (операция над всем массивом без цикла)
    multiplied_array: np.ndarray = numpy_array * 2

    print("\nРезультат векторизованной операции (умножение на 2):")
    print(f"  {multiplied_array}")


if __name__ == "__main__":
    main()