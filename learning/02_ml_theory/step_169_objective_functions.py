"""
Микро-шаг 169: Objective Functions.
Демонстрация связи между бизнес-целями, ML-метриками и целевыми функциями.
В ML это используется для выбора правильной функции потерь (loss function),
которую модель будет оптимизировать во время обучения.
"""


# Словарь: тип задачи -> целевая функция -> когда использовать
objective_functions: dict[str, dict[str, str]] = {
    "Regression (Регрессия)": {
        "MSE (Mean Squared Error)": "Штрафует большие ошибки сильнее, чувствительна к выбросам",
        "MAE (Mean Absolute Error)": "Устойчива к выбросам, интерпретируема",
        "Huber Loss": "Компромисс между MSE и MAE, менее чувствительна к выбросам"
    },
    "Binary Classification (Бинарная классификация)": {
        "Binary Cross-Entropy": "Стандарт для бинарной классификации, работает с вероятностями",
        "Hinge Loss (SVM)": "Максимизирует зазор между классами, используется в SVM"
    },
    "Multi-class Classification (Многоклассовая классификация)": {
        "Categorical Cross-Entropy": "Стандарт для многоклассовой классификации",
        "Sparse Categorical Cross-Entropy": "Когда метки — целые числа, а не one-hot"
    }
}


def print_objective_functions() -> None:
    """Выводит целевые функции для разных типов задач."""
    print("Целевые функции (Objective Functions) в машинном обучении:\n")

    for task_type, functions in objective_functions.items():
        print(f"🔹 {task_type}:")
        for func_name, description in functions.items():
            print(f"  - {func_name}")
            print(f"    → {description}")
        print()


def demonstrate_business_vs_ml_objective() -> None:
    """Показывает разницу между бизнес-метрикой и ML-целевой функцией."""
    print("Бизнес-метрика и ML-целевая функция:")
    print()
    print("Пример:")
    print("  Бизнес-цель: Максимизировать прибыль от подписок")
    print("  Бизнес-метрика: Monthly Recurring Revenue (MRR)")
    print("  ML-задача: Предсказать, отменит ли клиент подписку")
    print("  ML-целевая функция: Binary Cross-Entropy (минимизируем)")
    print("  ML-метрика: F1-score или AUC-ROC (максимизируем)")
    print()
    print("Почему не совпадают?")
    print("  - Бизнес-метрика часто недифференцируема (нельзя оптимизировать градиентом)")
    print("  - ML-целевая функция должна быть математически удобной для оптимизации")
    print("  - ML-метрика ближе к бизнес-цели, но используется для оценки, не обучения")


if __name__ == "__main__":
    print_objective_functions()
    demonstrate_business_vs_ml_objective()