"""Тесты для класса AnonymousSurvey из шага 155 (с использованием setUp)."""
import unittest

from tutorials.step_155_testing_class import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Тесты для класса AnonymousSurvey."""

    def setUp(self) -> None:
        """Создаёт объект опроса и список ответов для использования во всех тестах."""
        question: str = "Какой язык программирования вы хотите изучить?"
        self.survey: AnonymousSurvey = AnonymousSurvey(question)
        self.responses: list[str] = ["Python", "Java", "C++"]

    def test_store_single_response(self) -> None:
        """Тестирует сохранение одного ответа."""
        self.survey.store_response("Python")
        self.assertIn("Python", self.survey.responses)

    def test_store_multiple_responses(self) -> None:
        """Тестирует сохранение нескольких ответов."""
        for response in self.responses:
            self.survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.survey.responses)


if __name__ == '__main__':
    unittest.main()