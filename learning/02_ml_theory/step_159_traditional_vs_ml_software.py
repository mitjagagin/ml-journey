"""
Микро-шаг 159: Традиционное ПО против ML-систем (Traditional vs ML Software).
Сравнение жестко заданных правил (if/else) и вероятностного подхода на основе данных.
В ML это базовое отличие: традиционное ПО детерминировано, а ML-системы
вероятностны и зависят от качества данных, а не только от правильности кода.
"""

# Жестко заданные правила для традиционного фильтра (детерминированный подход)
def traditional_spam_filter(email_text: str) -> str:
    """Возвращает 'Спам' или 'Не спам' на основе точных совпадений."""
    if "купите" in email_text and "бесплатно" in email_text:
        return "Спам"
    return "Не спам"

# Словарь "весов" признаков, обученный на исторических данных (вероятностный подход).
# В реальных ML-моделях эти веса хранятся в массивах (NumPy), но мы используем словарь.
feature_weights: dict[str, float] = {
    "купите": 0.8,
    "бесплатно": 0.5,
    "срочно": 0.2,
    "отчет": -0.5,
    "встреча": -0.5,
}

def ml_spam_filter(email_text: str, threshold: float = 0.7) -> str:
    """Считает оценку спама на основе суммы весов найденных признаков."""
    spam_score: float = 0.0
    words: list[str] = email_text.split()

    for word in words:
        if word in feature_weights:
            spam_score += feature_weights[word]

    if spam_score >= threshold:
        return f"Спам (оценка: {spam_score})"
    return f"Не спам (оценка: {spam_score})"

# Тестовые данные (входные признаки)
emails: list[str] = [
    "купите прямо сейчас бесплатно",
    "срочно купите наш продукт",
    "завтра встреча и отчет по проекту",
    "бесплатно срочно купите",
]

print("Результаты классификации писем:")
print("")

for email in emails:
    traditional_result: str = traditional_spam_filter(email)
    ml_result: str = ml_spam_filter(email)

    print(f"Письмо: '{email}'")
    print(f"  Традиционное ПО: {traditional_result}")
    print(f"  ML-система:      {ml_result}")
    print("")