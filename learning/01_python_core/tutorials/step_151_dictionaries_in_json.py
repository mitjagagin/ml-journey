"""
Микро-шаг 151: Словари в формате JSON (Dictionaries in JSON).
Сохранение и загрузка словарей Python в формате JSON.
В ML словари используются для хранения конфигов (файлов с настройками модели).
В таких файлах часто лежат гиперпараметры (настройки, которые человек
задаёт до начала обучения).
"""
import json
from pathlib import Path

# Словарь с настройками (гиперпараметрами) для обучения модели
model_config: dict = {
    "learning_rate": 0.01,
    "epochs": 10,
    "optimizer": "adam"
}

# Путь к файлу конфигурации
path: Path = Path("model_config.json")

# 1. Сохраняем словарь в JSON-файл
with open(path, "w") as file_object:
    json.dump(model_config, file_object)

# 2. Загружаем словарь обратно из JSON-файла
with open(path) as file_object:
    loaded_config: dict = json.load(file_object)

print("Загруженный конфиг модели:")
# Проходим по всем парам ключ-значение загруженного словаря
for key, value in loaded_config.items():
    print(f"  {key}: {value}")