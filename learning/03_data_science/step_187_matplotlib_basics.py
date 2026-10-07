"""
Микро-шаг 187: Основы визуализации данных с Matplotlib (Matplotlib Basics).
Построение линейного графика и диаграммы рассеяния (scatter plot).
В ML это используется для разведочного анализа данных (EDA) и визуализации метрик обучения.
"""

import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    # Генерируем синтетические данные с помощью NumPy
    x_values: np.ndarray = np.linspace(start=0.0, stop=10.0, num=50)

    # 1. Линейный график (Line plot)
    # Имитируем кривую обучения или тренд
    y_line: np.ndarray = np.sin(x_values)

    plt.figure(figsize=(8, 4))
    plt.plot(x_values, y_line, color="blue", label="sin(x)")
    plt.title("Линейный график (например, кривая обучения)")
    plt.xlabel("Эпохи (или время)")
    plt.ylabel("Значение метрики")
    plt.legend()
    plt.grid(True)

    print("Отображение линейного графика... (закройте окно для продолжения)")
    plt.show()

    # 2. Диаграмма рассеяния (Scatter plot)
    # Имитируем распределение объектов в пространстве признаков
    np.random.seed(seed=42)
    x_scatter: np.ndarray = np.random.rand(50) * 10
    y_scatter: np.ndarray = x_scatter * 2 + np.random.randn(50) * 1.5  # Линейная зависимость + шум

    plt.figure(figsize=(8, 4))
    plt.scatter(x_scatter, y_scatter, color="red", alpha=0.7, label="Данные с шумом")
    plt.title("Диаграмма рассеяния (например, зависимость признаков)")
    plt.xlabel("Признак X (Feature 1)")
    plt.ylabel("Целевая переменная Y (Target)")
    plt.legend()
    plt.grid(True)

    print("Отображение диаграммы рассеяния... (закройте окно для завершения)")
    plt.show()


if __name__ == "__main__":
    main()