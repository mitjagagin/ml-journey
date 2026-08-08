# 🚀 ML/AI Engineering Journey

Персональный проект по пути от абсолютного нуля до Junior/Middle AI Engineer.

## 📍 Текущий статус
- **Этап:** 0 — Фундамент: Python Core + ML-основы + математика (4-5 недель, интегрированный)
- **Прогресс:** Matthes Ch.1-4 завершены полностью. В Главе 5 пройдены 5.1-5.3.6, 5.4.1-5.4.2 (шаги 49-65). Осталось: 5.4.3 и 5.5.
- **Стек:** Python 3.10, Miniconda, PyCharm, Git, Docker Desktop
- **Следующий шаг:** Matthes 5.4.3 (Using Multiple Lists)
- **Общий горизонт:** ~12 месяцев (реалистичный срок)

## 🎯 Цель проекта
Построить 5 production-ready ML/AI проектов для портфолио:
1. **Wine Classifier** — классический ML (sklearn, RandomForest)
2. **House Price Predictor** — FastAPI + Docker
3. **Sentiment Analyzer API** — MLOps, CI/CD, AWS
4. **RAG Chatbot** — векторные БД, эмбеддинги
5. **LLM Twin** — fine-tuning (SFT/QLoRA/DPO) на Google Colab

## 📚 База знаний

### Книги (основные)
- **Python:** Eric Matthes — *Python Crash Course (3rd ed.)*
- **ML Engineering:** Andrew P. McMahon — *Machine Learning Engineering with Python (2nd ed.)*
- **ML Systems:** Chip Huyen — *Designing ML Systems*
- **AI Engineering:** Chip Huyen — *AI Engineering*
- **MLOps:** Noah Gift — *Practical MLOps*
- **LLM Engineering:** Paul Iusztin — *LLM Engineer's Handbook*

### Внешние ресурсы (точечно)
- **Pandas:** Kaggle Learn (интерактивный курс, 4 часа)
- **SQL:** SQLZoo (интерактивный курс, 5-6 часов)
- **Линейная алгебра:** 3Blue1Brown — *Essence of Linear Algebra* (15 видео, 3-4 часа)
- **Hugging Face:** HF NLP Course (официальный, 10-12 часов)

## 🛠️ Технологии и практики
- **Язык:** Python 3.10 (type hints, docstrings, PEP 8)
- **Окружение:** Miniconda (conda env `ml_zero`)
- **IDE:** PyCharm Professional
- **VCS:** Git + GitHub (атомарные коммиты, Conventional Commits)
- **Контейнеризация:** Docker Desktop
- **Структура проекта:** `src/` (продакшен), `tutorials/` (учебные скрипты), `tests/`, `data/`, `notebooks/`
- **Стандарт оформления:** Строгий нейминг `step_NN_snake_case_name.py` и единый формат docstring для учебных скриптов.

## 📂 Структура проекта

    ml-journey/
    ├── src/                  # Продакшен-код (ML-пайплайны, модели)
    ├── tutorials/            # Учебные скрипты по Matthes (65+ файлов)
    ├── tests/                # Unit-тесты (pytest)
    ├── data/                 # Датасеты
    ├── notebooks/            # Jupyter-ноутбуки для EDA
    ├── COURSE_PLAN.md        # Детальный план курса с подглавами
    ├── ROADMAP.md            # Карта из 5 проектов-вех
    ├── LEARNING_JOURNAL.md   # Инженерное портфолио
    ├── GIT_WORKFLOW.md       # Правила атомарных коммитов
    └── README.md             # Этот файл

## 📊 Прогресс изучения

### Python (Matthes)
- ✅ Глава 1: Getting Started
- ✅ Глава 2: Variables and Simple Data Types
- ✅ Глава 3: Introducing Lists (полностью)
- ✅ Глава 4: Working with Lists (полностью: Slicing, Copying Lists, Tuples, Styling Code)
- 🔄 Глава 5: if Statements (пройдены 5.1-5.3.6, 5.4.1-5.4.2; осталось 5.4.3, 5.5)
- ⏳ Глава 6-11: Dictionaries, Functions, Classes, Files, Testing

### ML/AI Engineering
- ⏳ McMahon Ch.1-2: Introduction to ML Engineering
- ⏳ Huyen DMLS Ch.1-4: ML Systems, Data Engineering, Feature Engineering, Model Development
- ⏳ Проект 1: Wine Classifier (baseline)

### Data Science (Python)
- ⏳ Kaggle Learn: Pandas
- ⏳ NumPy, Matplotlib, Seaborn (ментор)

### Математика для ML
- ⏳ 3Blue1Brown: Essence of Linear Algebra
- ⏳ Статистика и теория вероятностей (ментор)

### Инженерные основы
- ⏳ SQLZoo (SQL)
- ⏳ HTTP/API, Linux/Bash, продвинутый Git (ментор)

## 🗺️ Этапы курса

| Этап | Название | Длительность | Статус |
|------|----------|--------------|--------|
| 0 | Фундамент: Python Core + ML-основы + математика | 4-5 недель (интегрированный) | 🔄 В процессе |
| 1 | Первый ML-проект: Wine Classifier | 2-3 недели | ⚪ Ожидает |
| 2 | ML as a Service: House Price Predictor | 3-4 недели | ⚪ Ожидает |
| 3 | MLOps + Cloud: Sentiment Analyzer API | 4-5 недель | ⚪ Ожидает |
| 4 | Foundation Models + RAG | 5-6 недель | ⚪ Ожидает |
| 5 | Fine-tuning + Production: LLM Twin | 5-6 недель | ⚪ Ожидает |

## 🔗 Ссылки
- **GitHub:** [mitjagagin/ml-journey](https://github.com/mitjagagin/ml-journey)
- **Conda env:** `ml_zero` (Python 3.10, numpy, pandas, scikit-learn, pytest)

## 📝 Правила работы
- **Темп:** Микро-шаги с подтверждением (один шаг → "готово" → следующий)
- **Коммиты:** Атомарные, по `GIT_WORKFLOW.md` (Conventional Commits)
- **Код:** Type hints, docstrings, структура `src/` vs `tutorials/`
- **Документация:** Обновление `LEARNING_JOURNAL.md` после каждого этапа

---
**Статус:** Активная разработка
**Последнее обновление:** 2026-08-08