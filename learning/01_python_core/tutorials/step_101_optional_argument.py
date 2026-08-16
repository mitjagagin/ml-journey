"""
Микро-шаг 101: Необязательный аргумент (Making an Argument Optional).
Параметр со значением по умолчанию, который можно не передавать.
В ML это используется, когда не все параметры нужны для каждого запуска:
например, идентификатор эксперимента может отсутствовать.
"""

# Функция с необязательным параметром experiment_id
# По умолчанию пустая строка означает "параметр не передан"
def get_experiment_name(model_name: str, dataset_name: str, experiment_id: str = "") -> str:
    if experiment_id != "":
        full_name: str = f"{model_name}_{dataset_name}_{experiment_id}"
    else:
        full_name: str = f"{model_name}_{dataset_name}"
    return full_name

# Вызов БЕЗ необязательного параметра
name_without_id: str = get_experiment_name("RandomForest", "Wine")
print("Без идентификатора:")
print(f"  {name_without_id}")

# Вызов С необязательным параметром
name_with_id: str = get_experiment_name("RandomForest", "Wine", "exp_042")
print("\nС идентификатором:")
print(f"  {name_with_id}")