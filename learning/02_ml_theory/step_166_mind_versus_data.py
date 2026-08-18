"""
Микро-шаг 166: Mind Versus Data.
Два фундаментальных подхода к решению задач:
- Mind (rule-based): инженер пишет явные правила.
- Data (data-driven): модель учится на данных.
В ML-инженерии выбор между ними определяет архитектуру всей системы:
правила быстры и интерпретируемы, но не масштабируются;
данные требуют ресурсов, но лучше обобщают и адаптируются.
"""

# Rule-based (Mind) подход: функция с явными правилами для определения спама.
# Инженер вручную описал признаки, по которым письмо считается спамом.
def is_spam_by_rules(subject: str, body: str) -> bool:
    """Определяет, является ли письмо спамом, по набору жёстких правил."""
    spam_keywords: list[str] = ["бесплатно", "выигрыш", "срочно", "click here", "prize"]
    subject_lower: str = subject.lower()
    body_lower: str = body.lower()
    for keyword in spam_keywords:
        if keyword in subject_lower or keyword in body_lower:
            return True
    return False


# Тестовые письма для проверки rule-based подхода.
test_emails: list[dict[str, str]] = [
    {"subject": "Встреча в понедельник", "body": "Привет, обсудим проект в 15:00."},
    {"subject": "Бесплатно! Вы выиграли приз", "body": "Click here to claim your prize."},
    {"subject": "Отчёт за квартал", "body": "Во вложении финансовые показатели."},
    {"subject": "Срочно! Срочно!", "body": "Переведите деньги на счёт немедленно."},
]

print("Rule-based (Mind) подход — спам-фильтр на правилах:")
for email in test_emails:
    result: bool = is_spam_by_rules(email["subject"], email["body"])
    label: str = "СПАМ" if result else "НЕ СПАМ"
    print(f"  Тема: {email['subject'][:40]}... → {label}")

# Сравнение подходов Mind и Data.
approaches: dict[str, dict[str, str]] = {
    "Mind (rule-based)": {
        "principle": "Инженер пишет явные правила решения задачи",
        "pros": "Быстро, интерпретируемо, не требует данных",
        "cons": "Не масштабируется, хрупкий, не обобщает",
        "when_to_use": "Простые детерминированные задачи (валидация формата, базовые фильтры)"
    },
    "Data (data-driven)": {
        "principle": "Модель учится находить закономерности из данных",
        "pros": "Масштабируется, обобщает, адаптируется к изменениям",
        "cons": "Требует данных, вычислительных ресурсов, сложнее отлаживать",
        "when_to_use": "Сложные задачи с неочевидными закономерностями (распознавание образов, NLP, рекомендации)"
    }
}

print("\nСравнение подходов:")
for name, details in approaches.items():
    print(f"{name}:")
    print(f"  Принцип:    {details['principle']}")
    print(f"  Плюсы:      {details['pros']}")
    print(f"  Минусы:     {details['cons']}")
    print(f"  Когда юзать: {details['when_to_use']}\n")