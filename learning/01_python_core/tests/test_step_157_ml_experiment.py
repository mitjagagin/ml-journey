"""Тесты для класса MLExperiment из шага 157."""
import unittest

from tutorials.step_157_ml_experiment import MLExperiment


class TestMLExperiment(unittest.TestCase):
    """Тесты для класса MLExperiment."""

    def setUp(self) -> None:
        """Создаёт свежий эксперимент перед каждым тестом."""
        self.experiment: MLExperiment = MLExperiment("LogisticRegression")

    def test_add_result(self) -> None:
        """Тестирует добавление одной метрики."""
        self.experiment.add_result("accuracy", 0.92)
        self.assertEqual(self.experiment.get_result("accuracy"), 0.92)

    def test_get_missing_metric(self) -> None:
        """Тестирует получение метрики, которой нет."""
        self.assertEqual(self.experiment.get_result("recall"), 0.0)

    def test_has_metric(self) -> None:
        """Тестирует проверку наличия метрики."""
        self.experiment.add_result("f1_score", 0.89)
        self.assertTrue(self.experiment.has_metric("f1_score"))
        self.assertFalse(self.experiment.has_metric("recall"))

    def test_multiple_results(self) -> None:
        """Тестирует добавление нескольких метрик."""
        self.experiment.add_result("accuracy", 0.92)
        self.experiment.add_result("f1_score", 0.89)
        self.experiment.add_result("recall", 0.91)

        self.assertEqual(len(self.experiment.results), 3)
        self.assertIn("recall", self.experiment.results)


if __name__ == '__main__':
    unittest.main()