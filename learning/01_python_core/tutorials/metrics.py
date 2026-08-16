"""
Модуль с классами метрик (числовых оценок качества модели).
Содержит три связанных класса для оценки классификаторов.
"""


class Accuracy:
    """Метрика accuracy (доля правильных предсказаний)."""

    def __init__(self) -> None:
        """Инициализация метрики."""
        self.name: str = "Accuracy"

    def calculate(self, correct: int, total: int) -> float:
        """Вычисление accuracy."""
        return correct / total

    def describe(self) -> None:
        """Вывод описания метрики."""
        print(f"  Метрика: {self.name} (доля правильных предсказаний)")


class Precision:
    """Метрика precision (точность: доля истинно положительных среди всех положительных предсказаний)."""

    def __init__(self) -> None:
        """Инициализация метрики."""
        self.name: str = "Precision"

    def calculate(self, true_positives: int, false_positives: int) -> float:
        """Вычисление precision."""
        if true_positives + false_positives == 0:
            return 0.0
        return true_positives / (true_positives + false_positives)

    def describe(self) -> None:
        """Вывод описания метрики."""
        print(f"  Метрика: {self.name} (точность положительных предсказаний)")


class Recall:
    """Метрика recall (полнота: доля истинно положительных среди всех реальных положительных)."""

    def __init__(self) -> None:
        """Инициализация метрики."""
        self.name: str = "Recall"

    def calculate(self, true_positives: int, false_negatives: int) -> float:
        """Вычисление recall."""
        if true_positives + false_negatives == 0:
            return 0.0
        return true_positives / (true_positives + false_negatives)

    def describe(self) -> None:
        """Вывод описания метрики."""
        print(f"  Метрика: {self.name} (полнота обнаружения положительных примеров)")