"""
Микро-шаг 56: Проверка отсутствия значения в списке (Value Not in List).
Оператор not in проверяет, что элемент отсутствует в списке.
В ML это используется для blacklist-фильтрации: исключение нежелательных
значений из обработки, например запрещённых классов или критических статусов.
"""

# Запрещённые классы для модели классификации
banned_classes: list[str] = ["spam", "fraud", "abuse"]

# Класс, который пришёл для обработки
incoming_class: str = "normal"

# Проверка через not in: отсутствует ли значение в списке
print("Проверка входящего класса:")
if incoming_class not in banned_classes:
    print(f"  Класс '{incoming_class}' разрешён для обработки")
else:
    print(f"  Класс '{incoming_class}' заблокирован")

# Класс, который есть в чёрном списке
suspicious_class: str = "spam"

print("\nПроверка подозрительного класса:")
if suspicious_class not in banned_classes:
    print(f"  Класс '{suspicious_class}' разрешён для обработки")
else:
    print(f"  Класс '{suspicious_class}' заблокирован")

# Статусы, при которых нужно немедленно остановить пайплайн
critical_statuses: list[str] = ["failed", "corrupted", "timeout"]
current_status: str = "running"

print("\nПроверка статуса пайплайна:")
if current_status not in critical_statuses:
    print(f"  Статус '{current_status}' — пайплайн продолжает работу")
else:
    print(f"  Статус '{current_status}' — требуется немедленная остановка")