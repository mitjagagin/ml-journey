"""
Микро-шаг 61: Использование нескольких elif блоков (Using Multiple elif Blocks).
Каждый elif проверяет отдельное условие, позволяя строить
многоуровневую классификацию. В ML это применяется для градации
уровней важности алертов мониторинга и оценки качества модели по диапазонам.
"""

# Уровень важности инцидента в мониторинге ML-систем
incident_severity: str = "warning"

# Правила реагирования на разные уровни
print("Реагирование на инцидент:")
if incident_severity == "critical":
    print("  Немедленная остановка пайплайна, алерт всей команде")
elif incident_severity == "error":
    print("  Алерт дежурному инженеру в течение 15 минут")
elif incident_severity == "warning":
    print("  Запись в лог, проверка при следующем запуске")
elif incident_severity == "info":
    print("  Только запись в лог, без уведомлений")
else:
    print("  Неизвестный уровень инцидента")

# Классификация качества модели по диапазонам accuracy
model_accuracy: int = 78

print("\nКлассификация качества модели:")
if model_accuracy >= 90:
    print(f"  Accuracy {model_accuracy}% — отличное качество")
elif model_accuracy >= 75:
    print(f"  Accuracy {model_accuracy}% — приемлемое качество")
elif model_accuracy >= 60:
    print(f"  Accuracy {model_accuracy}% — требует доработки")
else:
    print(f"  Accuracy {model_accuracy}% — неприемлемо, переобучение")

# Тестирование всех уровней инцидентов в цикле
severities_to_test: list[str] = ["critical", "error", "warning", "info", "unknown"]

print("\nТестирование всех уровней:")
for severity in severities_to_test:
    if severity == "critical":
        print(f"  {severity}: стоп пайплайн")
    elif severity == "error":
        print(f"  {severity}: алерт дежурному")
    elif severity == "warning":
        print(f"  {severity}: запись в лог")
    elif severity == "info":
        print(f"  {severity}: только лог")
    else:
        print(f"  {severity}: неизвестный уровень")