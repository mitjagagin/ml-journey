# 🚀 ML/AI Engineering Journey

Персональный проект по пути от абсолютного нуля до Junior/Middle AI Engineer.

## 📍 Текущий статус
- **Этап:** 0 — Фундамент: Python Core + ML-основы + математика (4-5 недель, интегрированный)
- **Прогресс:** Matthes Ch.1-11 закрыты полностью (включая Главу 11: Testing Your Code) — 158 учебных скриптов. Детальный план со всеми подглавами — в [`COURSE_PLAN.md`](COURSE_PLAN.md).
- **Стек:** Python 3.10, Miniconda, PyCharm, Git, Docker Desktop
- **Следующий шаг:** Переход к Колее 2 (ML-теория: Huyen DMLS Ch.1-4)
- **Общий горизонт:** ~12 месяцев (реалистичный срок)

## 🎯 Цель проекта
Построить 5 production-ready ML/AI проектов для портфолио (детальная карта — в [`ROADMAP.md`](ROADMAP.md)):
1. **Wine Classifier** — классический ML (sklearn, RandomForest)
2. **House Price Predictor** — FastAPI + Docker
3. **Sentiment Analyzer API** — MLOps, CI/CD, AWS
4. **RAG Chatbot** — векторные БД, эмбеддинги
5. **LLM Twin (Production-ready)** — fine-tuning (SFT/QLoRA/DPO) на Google Colab

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
- **Структура проекта:** `src/` (продакшен), `learning/` (учебные треки), `projects/` (проекты-вехи), `tests/`, `data/`, `notebooks/`
- **Стандарт оформления:** Строгий нейминг `step_NN_snake_case_name.py` и единый формат docstring для учебных скриптов.

## 📂 Структура проекта

```text
ml-journey/
├── learning/                 # Учебные треки
│   ├── 01_python_core/       # Python (Matthes Ch.1-11)
│   │   ├── tutorials/        # 158 учебных скриптов
│   │   └── tests/            # Unit-тесты к скриптам
│   ├── 02_ml_theory/         # ML-теория (Huyen DMLS)
│   ├── 03_data_science/      # pandas, NumPy, Matplotlib
│   ├── 04_math_for_ml/       # Линейная алгебра, статистика
│   └── 05_engineering_basics/# SQL, HTTP/API, bash, Git
├── projects/                 # 5 проектов-вех (см. ROADMAP.md)
├── src/                      # Продакшен-код (общий для проектов)
├── tests/                    # Тесты для проектов (src/)
├── data/                     # Датасеты
│   └── raw/                  # Исходные (неизменяемые) данные
├── notebooks/                # Jupyter-ноутбуки для EDA
├── COURSE_PLAN.md            # Детальный план курса (источник истины)
├── ROADMAP.md                # Карта из 5 проектов-вех
├── LEARNING_JOURNAL.md       # Инженерное портфолио
├── GIT_WORKFLOW.md           # Правила атомарных коммитов
└── README.md                 # Этот файл
```

## 🔗 Ссылки
- **GitHub:** [mitjagagin/ml-journey](https://github.com/mitjagagin/ml-journey)
- **Conda env:** `ml_zero` (Python 3.10, numpy, pandas, scikit-learn, pytest)

## 📝 Правила работы
- **Темп:** Микро-шаги с подтверждением (один шаг → "готово" → следующий)
- **Коммиты:** Атомарные, по `GIT_WORKFLOW.md` (Conventional Commits)
- **Код:** Type hints, docstrings, структура `src/` vs `learning/`
- **Документация:** Обновление `LEARNING_JOURNAL.md` после каждого этапа

---
**Статус:** Активная разработка
**Последнее обновление:** 2026-08-16