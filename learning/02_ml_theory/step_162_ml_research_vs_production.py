"""
Микро-шаг 162: ML в исследовании и в продакшене (ML in Research vs Production).
Сравнение выбора модели только по метрике качества и выбора с учетом производственных ограничений.
В ML это важно: лучшая модель в исследовании может не подойти для реального сервиса,
если она слишком медленная, дорогая или нестабильная.
"""

# Список моделей-кандидатов
model_names: list[str] = [
    "Model A (SOTA)",
    "Model B (baseline)",
    "Model C (small)",
]

# Точность модели: доля правильных ответов
accuracies: list[float] = [0.95, 0.91, 0.88]

# Задержка предсказания в миллисекундах
latencies_ms: list[float] = [450.0, 40.0, 12.0]

def choose_best_for_research(names: list[str], scores: list[float]) -> str:
    """Возвращает модель с максимальной метрикой без других ограничений."""
    best_index: int = 0

    for i in range(len(scores)):
        if scores[i] > scores[best_index]:
            best_index = i

    return names[best_index]

def choose_best_for_production(names: list[str], scores: list[float], latencies: list[float], max_latency_ms: float) -> str:
    """Возвращает лучшую модель среди тех, кто проходит ограничение по задержке."""
    eligible_names: list[str] = []
    eligible_scores: list[float] = []

    # Отбираем модели, которые отвечают требованию production по скорости
    for i in range(len(names)):
        if latencies[i] <= max_latency_ms:
            eligible_names.append(names[i])
            eligible_scores.append(scores[i])

    # Если ни одна модель не прошла ограничение
    if len(eligible_names) == 0:
        return "Нет подходящей модели"

    best_index: int = 0

    for i in range(len(eligible_scores)):
        if eligible_scores[i] > eligible_scores[best_index]:
            best_index = i

    return eligible_names[best_index]

print("Выбор ML-модели: research vs production:")
print("")

research_best: str = choose_best_for_research(model_names, accuracies)

print("Research-подход:")
print(f"  Лучшая модель: {research_best}")
print("  Причина: максимальная accuracy без учета ограничений продакшена.")
print("")

max_latency_ms: float = 100.0
production_best: str = choose_best_for_production(model_names, accuracies, latencies_ms, max_latency_ms)

print("Production-подход:")
print(f"  Ограничение: latency <= {max_latency_ms} ms")
print(f"  Лучшая модель: {production_best}")
print("  Причина: модель проходит ограничение по задержке и имеет лучшую accuracy среди допустимых.")
print("")

print("Вывод:")
print("  Модель с лучшей метрикой в исследовании может не подойти для продакшена.")