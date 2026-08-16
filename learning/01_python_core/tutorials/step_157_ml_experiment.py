"""
Микро-шаг 157: Проект — класс ML-эксперимента.
Класс для хранения результатов обучения модели.
В ML такие классы используются для сравнения разных моделей
и выбора лучшей по метрикам (числовым оценкам качества).
"""


class MLExperiment:
    """Класс для хранения результатов обучения одной модели."""

    def __init__(self, model_name: str) -> None:
        """Инициализирует эксперимент с именем модели."""
        self.model_name: str = model_name
        self.results: dict[str, float] = {}

    def add_result(self, metric_name: str, value: float) -> None:
        """Добавляет результат по одной метрике."""
        self.results[metric_name] = value

    def get_result(self, metric_name: str) -> float:
        """Возвращает значение конкретной метрики."""
        return self.results.get(metric_name, 0.0)

    def has_metric(self, metric_name: str) -> bool:
        """Проверяет, есть ли метрика в результатах."""
        return metric_name in self.results

    def summary(self) -> None:
        """Выводит сводку по всем метрикам эксперимента."""
        print(f"Эксперимент: {self.model_name}")
        if not self.results:
            print("  Нет сохранённых метрик")
            return

        for metric_name, value in self.results.items():
            print(f"  {metric_name}: {value}")


# Демонстрация работы класса
if __name__ == "__main__":
    # Создаём эксперимент для модели LogisticRegression
    exp1 = MLExperiment("LogisticRegression")
    exp1.add_result("accuracy", 0.92)
    exp1.add_result("f1_score", 0.89)
    exp1.summary()

    # Создаём эксперимент для модели RandomForest
    exp2 = MLExperiment("RandomForest")
    exp2.add_result("accuracy", 0.95)
    exp2.add_result("f1_score", 0.93)
    exp2.add_result("recall", 0.91)
    exp2.summary()

    # Проверяем наличие метрики
    print(f"\nУ RandomForest есть recall: {exp2.has_metric('recall')}")
    print(f"У LogisticRegression есть recall: {exp1.has_metric('recall')}")

    # Получаем конкретную метрику
    rf_accuracy = exp2.get_result("accuracy")
    print(f"\nAccuracy у RandomForest: {rf_accuracy}")