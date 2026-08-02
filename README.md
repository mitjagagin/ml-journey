# 🚀 ML/AI Engineering Journey

Персональный проект по пути от абсолютного нуля до Junior/Middle AI Engineer.

## 📍 Текущий статус
- **Этап:** Python-база (Matthes Ch.2-3 завершены)
- **Прогресс:** Изучены переменные, строки, числа, списки, циклы for
- **Стек:** Python 3.10, Miniconda, PyCharm, Git, Docker Desktop
- **Следующий шаг:** Matthes Ch.4 (работа со списками, list comprehensions)

## 🎯 Цель проекта
Построить 5 production-ready ML/AI проектов для портфолио:
1. **Wine Classifier** — классический ML (sklearn, RandomForest)
2. **ML as a Service** — FastAPI + Docker
3. **RAG Chatbot** — векторные БД, эмбеддинги
4. **LLM Twin** — fine-tuning (SFT/QLoRA/DPO)
5. **Production Pipeline** — CI/CD, мониторинг, дрейф данных

## 📚 База знаний
- **Python:** Eric Matthes — *Python Crash Course (3rd ed.)*
- **ML Engineering:** Andrew P. McMahon — *Machine Learning Engineering with Python (2nd ed.)*
- **ML Systems:** Chip Huyen — *Designing ML Systems*
- **AI Engineering:** Chip Huyen — *AI Engineering*
- **MLOps:** Noah Gift — *Practical MLOps*
- **LLM Engineering:** Paul Iusztin — *LLM Engineer's Handbook*

## 🛠️ Технологии и практики
- **Язык:** Python 3.10 (type hints, docstrings, PEP 8)
- **Окружение:** Miniconda (conda env `ml_zero`)
- **IDE:** PyCharm Professional
- **VCS:** Git + GitHub (атомарные коммиты, Conventional Commits)
- **Контейнеризация:** Docker Desktop
- **Структура проекта:** `src/` (продакшен), `tutorials/` (учебные скрипты), `tests/`, `data/`, `notebooks/`

## 📂 Структура проекта

    ml-journey/
    ├── src/                  # Продакшен-код (ML-пайплайны, модели)
    ├── tutorials/            # Учебные скрипты по Matthes
    ├── tests/                # Unit-тесты (pytest)
    ├── data/                 # Датасеты
    ├── notebooks/            # Jupyter-ноутбуки для EDA
    ├── COURSE_PLAN.md        # Детальный план курса с подглавами
    ├── ROADMAP.md            # Карта из 5 проектов-вех
    ├── LEARNING_JOURNAL.md   # Инженерное портфолио
    └── GIT_WORKFLOW.md       # Правила атомарных коммитов

## 📊 Прогресс изучения

### Python (Matthes)
- ✅ Глава 1: Getting Started
- ✅ Глава 2: Variables and Simple Data Types
- 🔄 Глава 3: Introducing Lists (до 3.3.4)
- ⏳ Глава 4: Working with Lists

### ML/AI Engineering
- ⏳ McMahon Ch.1-2: Introduction to ML Engineering
- ⏳ Huyen DMLS Ch.1: Overview of ML Systems
- ⏳ Проект 1: Wine Classifier (baseline)

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
**Последнее обновление:** 2026-08-01