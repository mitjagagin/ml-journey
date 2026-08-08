"""
Микро-шаг 63: Проверка нескольких условий (Testing Multiple Conditions).
Последовательные if блоки проверяют все условия независимо друг от друга.
В ML это применяется для валидации данных, guardrails в LLM-системах
и мульти-критериальной оценки моделей.
"""

# Валидация входящего файла данных
file_size_mb: int = 150
file_format: str = "csv"
file_encoding: str = "utf-8"

print("Валидация файла данных:")
if file_size_mb > 100:
    print(f"  Размер файла {file_size_mb}MB превышает лимит 100MB")
if file_format != "csv":
    print(f"  Формат '{file_format}' не поддерживается, требуется CSV")
if file_encoding != "utf-8":
    print(f"  Кодировка '{file_encoding}' не поддерживается, требуется UTF-8")

# Guardrails для LLM-ответа (проверка нескольких нарушений)
llm_response: str = "Этот продукт содержит опасные вещества"
toxicity_score: float = 0.85
contains_pii: bool = True
hallucination_detected: bool = False

print("\nGuardrails для LLM-ответа:")
if toxicity_score > 0.7:
    print(f"  Токсичность {toxicity_score} превышает порог 0.7")
if contains_pii:
    print("  Обнаружена персональная информация (PII)")
if hallucination_detected:
    print("  Обнаружена галлюцинация модели")

# Мульти-критериальная оценка модели
model_accuracy: int = 92
model_latency_ms: int = 120
model_memory_mb: int = 256

# Целевые пороги
target_accuracy: int = 90
target_latency_ms: int = 100
target_memory_mb: int = 200

print("\nМульти-критериальная оценка модели:")
if model_accuracy >= target_accuracy:
    print(f"  Accuracy {model_accuracy}% >= {target_accuracy}% ✅")
else:
    print(f"  Accuracy {model_accuracy}% < {target_accuracy}% ❌")

if model_latency_ms <= target_latency_ms:
    print(f"  Latency {model_latency_ms}ms <= {target_latency_ms}ms ✅")
else:
    print(f"  Latency {model_latency_ms}ms > {target_latency_ms}ms ❌")

if model_memory_mb <= target_memory_mb:
    print(f"  Memory {model_memory_mb}MB <= {target_memory_mb}MB ✅")
else:
    print(f"  Memory {model_memory_mb}MB > {target_memory_mb}MB ❌")