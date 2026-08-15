"""
Микро-шаг 155: Тестирование класса (Testing a Class).
Класс для проведения анонимного опроса.
В ML подобные классы используются для управления конфигурацией
(настройками модели) или обработки метаданных.
"""


class AnonymousSurvey:
    """Класс для сбора анонимных ответов на вопрос."""

    def __init__(self, question: str) -> None:
        """Сохраняет вопрос."""
        self.question: str = question
        self.responses: list[str] = []

    def show_question(self) -> None:
        """Выводит вопрос."""
        print(f"Вопрос: {self.question}")

    def store_response(self, new_response: str) -> None:
        """Сохраняет один ответ."""
        self.responses.append(new_response)

    def show_results(self) -> None:
        """Выводит все ответы."""
        print("Результаты опроса:")
        for response in self.responses:
            print(f"  - {response}")


# Демонстрация работы класса
if __name__ == "__main__":
    survey = AnonymousSurvey("Какой язык программирования вы хотите изучить?")
    survey.show_question()

    print("\nСбор ответов...")
    survey.store_response("Python")
    survey.store_response("Java")
    survey.store_response("C++")

    print("\n")
    survey.show_results()