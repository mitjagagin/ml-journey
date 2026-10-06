"""
Микро-шаг 184: Генерация массивов в NumPy (NumPy Array Generation).
Создание массивов с помощью фабричных функций: zeros, ones, arange, linspace, random.
В ML это используется для инициализации весов моделей и генерации синтетических данных.
"""

import numpy as np


def main() -> None:
    # 1. Массивы из нулей и единиц
    zeros_array: np.ndarray = np.zeros(shape=(2, 3))
    ones_array: np.ndarray = np.ones(shape=(3, 2))

    print("Массив из нулей (2 строки, 3 столбца):")
    print(zeros_array)

    print("\nМассив из единиц (3 строки, 2 столбца):")
    print(ones_array)

    # 2. Последовательности чисел: arange и linspace
    # arange(start, stop, step) — аналог range(), но возвращает ndarray
    arange_array: np.ndarray = np.arange(start=0, stop=10, step=2)

    # linspace(start, stop, num) — num равномерно распределённых точек
    linspace_array: np.ndarray = np.linspace(start=0.0, stop=1.0, num=5)

    print("\nnp.arange(0, 10, 2):")
    print(f"  {arange_array}")

    print("\nnp.linspace(0.0, 1.0, num=5):")
    print(f"  {linspace_array}")

    # 3. Случайные числа (используется для инициализации весов в ML)
    # Устанавливаем seed для воспроизводимости результатов
    np.random.seed(seed=42)
    random_array: np.ndarray = np.random.random(size=(2, 2))

    print("\nСлучайный массив 2x2 (с seed=42):")
    print(random_array)


if __name__ == "__main__":
    main()