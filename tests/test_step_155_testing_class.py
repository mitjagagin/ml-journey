"""Тесты для класса AnonymousSurvey из шага 155."""
import unittest

from tutorials.step_155_testing_class import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Тесты для класса AnonymousSurvey."""

    def test_store_single_response(self) -> None:
        """Тестирует сохранение одного ответа."""
        question: str = "Какой язык программирования вы хотите изучить?"
        survey = AnonymousSurvey(question)
        survey.store_response("Python")

        self.assertIn("Python", survey.responses)

    def test_store_multiple_responses(self) -> None:
        """Тестирует сохранение нескольких ответов."""
        question: str = "Какой язык программирования вы хотите изучить?"
        survey = AnonymousSurvey(question)

        responses: list[str] = ["Python", "Java", "C++"]
        for response in responses:
            survey.store_response(response)

        self.assertEqual(len(survey.responses), 3)
        for response in responses:
            self.assertIn(response, survey.responses)


if __name__ == '__main__':
    unittest.main()