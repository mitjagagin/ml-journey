# 📚 АКТИВНЫЙ ПЛАН КУРСА: ML/AI Engineer

> **Принцип работы:** Этот файл содержит активную детализацию текущего этапа и текущий прогресс.  
> Полная справочная карта курса со всеми подсекциями хранится в `COURSE_PLAN_FULL.md`.  
> Актуальный прогресс текущего этапа фиксируется здесь.

## 🏷 Легенда маркеров (аудит скоупа)

| Маркер | Значение |
|---|---|
| `[x]` | Пройдено |
| `[~]` | В процессе |
| `[ ]` | Очередь этапа: изучаем в этой колее/этапе |
| `[skip]` | Вне скоупа Junior/Middle AI Engineer |
| `[covered]` | Покрыто в другой колее/этапе |

**Принцип «Пакетной поставки»:** Вся теория из одной главы книги изучается в ОДНОМ месте (либо в Этапе 0, либо целиком в одном Проекте). Никаких разрывов между теорией и практикой.

---

## 🟢 ЭТАП 0. Фундамент (4-5 недель)

### Колея 1: Python (Matthes) — ✅ АРХИВ

- **Ch.1-11 закрыты полностью** (158 скриптов). Детали: [`learning/01_python_core/README.md`](learning/01_python_core/README.md)

### Колея 2: ML-теория (Huyen DMLS, концептуальные главы) — 🎯 АКТИВНАЯ ЗОНА

**Глава 1: Overview of ML Systems**

- [x] 1.1 When to Use ML + Use Cases (эвристика «когда ML нужен, а когда нет» — шаги 160, 161)
- [x] 1.2 ML in Research vs Production (включая challenges — шаг 162)
- [x] 1.3 ML Systems vs Traditional Software (шаг 159)

**Глава 2: Introduction to ML Systems Design**

- [x] 2.1 Business and ML Objectives (шаг 163)
- [x] 2.2 Requirements: reliability, scalability, maintainability, adaptability (шаг 164)
- [x] 2.3 Iterative Process (шаг 165)
- [x] 2.4 Framing ML Problems + Types of ML Tasks (шаги 167, 168)
- [x] 2.5 Objective Functions (шаг 169)
- [x] 2.6 Mind Versus Data (шаг 166)

**Глава 3: Data Engineering Fundamentals**

- [x] 3.1 Data Sources (шаг 170)
- [x] 3.2 Data Formats (JSON, row/column-major, text/binary) (шаг 171)
- [x] 3.3 Data Models (relational, NoSQL, structured/unstructured) (шаг 172)
- [x] 3.4 Storage Engines and Processing (OLTP/OLAP, ETL) (шаг 173)
- [ ] 3.5 Modes of Dataflow (databases/services/real-time; batch vs stream)

*(Главы 4-6 DMLS перенесены целиком в Проект 1)*  
*(Главы 8-9, 10.1, 10.3 DMLS перенесены целиком в Проект 3)*

### Колея 3: Python для Data Science

- [ ] **Pandas** (Kaggle Learn: DataFrame, фильтрация, groupby, пропуски)
- [ ] **NumPy** (ndarray, срезы, broadcasting, linalg)
- [ ] **Matplotlib/Seaborn** (графики, распределения, heatmaps)

### Колея 4: Математика для ML

- [ ] **Линал** (3Blue1Brown + ментор: векторы, матрицы, dot product, нормы)
- [ ] **Статистика** (описательная, распределения, гипотезы, p-value, доверит. интервалы)
- [ ] **Теорвер** (события, условная вероятность, Байес, мат. ожидание, дисперсия)

### Колея 5: Инженерные основы

- [ ] **SQLZoo** (SELECT, JOIN, GROUP BY) • [skip] Индексы
- [ ] **HTTP/API** (REST, методы, JSON, requests)
- [ ] **Linux/Bash** (навигация, файлы, пайплайны, скрипты)
- [ ] **Продвинутый Git** (ветки, PR, rebase)

---

## 🟡 ЭТАП 1. Проект 1: Wine Classifier (3-4 недели) — КОМПАКТ

> Детали этапа хранятся в полной справочной карте `COURSE_PLAN_FULL.md`.

**Теория (изучается целиком в этом проекте):**

- [ ] McMahon Ch.1-2 (полностью: Intro to ML Eng, ML Dev Process)
- [ ] Huyen DMLS Ch.4-6 (полностью: Training Data, Feature Engineering, Model Development)

**Практика:**

- sklearn, EDA, Feature Eng, LogisticRegression/RandomForest, метрики, pytest, структура `src/`.

---

## 🟠 ЭТАП 2. Проект 2: House Price Predictor (3-4 недели) — КОМПАКТ

**Теория (изучается целиком в этом проекте):**

- [ ] McMahon Ch.3-4 (полностью: Model Factory, Packaging)
- [ ] Gift Ch.3 (контейнеры, serving over HTTP)

**Практика:**

- California Housing, Pipelines, joblib, FastAPI, Docker, unit-тесты API, MLflow.

---

## 🔵 ЭТАП 3. Проект 3: Sentiment Analyzer API (4-5 недель) — КОМПАКТ

**Теория (изучается целиком в этом проекте):**

- [ ] Gift Ch.1, 4-7, 11-12 (MLOps, CD, Monitoring, AWS, CLI, Case Studies)
- [ ] McMahon Ch.5-6 (Deployment Patterns, Scaling Up)
- [ ] Huyen DMLS Ch.8-9, 10.1, 10.3 (Drift, Continual Learning, Infrastructure)

**Практика:**

- TF-IDF + LogReg, FastAPI, Docker, GitHub Actions, AWS (EC2/Lambda), Evidently AI, резюме/LinkedIn.

---

## 🟣 ЭТАП 4. Проект 4: RAG Chatbot (5-6 недель) — КОМПАКТ

**Теория (изучается целиком в этом проекте):**

- [ ] HF NLP Course (полностью)
- [ ] Huyen AI Ch.1-6 (Foundation Models, Evaluation, Prompt Eng, RAG)
- [ ] Iusztin Ch.1-4 (LLM Twin Concept, Tooling, Data Eng, RAG Pipeline)

**Практика:**

- Парсинг, чанкинг, ChromaDB, RAG-пайплайн, Streamlit/Gradio, Kaggle.

---

## 🔴 ЭТАП 5. Проект 5: LLM Twin (5-6 недель) — КОМПАКТ

**Теория (изучается целиком в этом проекте):**

- [ ] Iusztin Ch.5-11 + Приложение (SFT, DPO, Evaluation, Inference, Deployment, LLMOps)
- [ ] Huyen AI Ch.7-10 (Finetuning, Dataset Eng, Inference Opt, Architecture)

**Практика (на Google Colab):**

- SFT/QLoRA, DPO, Guardrails, Docker, CometML, A/B, LeetCode/Mock interviews.

---

## 🎯 Общая длительность

**~12 месяцев (реалистичный горизонт)**