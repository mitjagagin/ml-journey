"""
Микро-шаг 129: Импорт всего модуля (Importing an Entire Module).
Импорт модуля целиком и обращение к классам через точку (module.ClassName).
В ML это используется в больших проектах, чтобы явно видеть происхождение класса
и избежать конфликтов имён между разными модулями.
"""

# Импорт ВСЕГО модуля evaluators одной командой
import evaluators

print("Импорт всего модуля:")

# Обращение к классам через имя модуля + точку
cv: evaluators.CrossValidator = evaluators.CrossValidator(num_folds=5)
holdout: evaluators.HoldoutEvaluator = evaluators.HoldoutEvaluator(test_size=0.2)

# Описание оценщиков
print("\nСозданные оценщики:")
cv.describe()
holdout.describe()

# Использование методов импортированных классов
print("\nЗапуск оценки модели:")
cv.evaluate(model_name="Random Forest")
holdout.evaluate(model_name="Random Forest")

# Проверка состояния после использования
print("\nСостояние после оценки:")
cv.describe()
holdout.describe()