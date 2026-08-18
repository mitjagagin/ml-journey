# 📚 АКТИВНЫЙ ПЛАН КУРСА: ML/AI Engineer

> **Принцип работы:** Этот файл содержит детализацию только для *текущего* этапа. 
> Полная карта курса со всеми подсекциями хранится в `COURSE_PLAN_FULL.md` (раскрывается при входе в новый этап).
> Прогресс `[x]` ставится только здесь.

## 🏷 Легенда маркеров (аудит скоупа)

| Маркер | Значение |
|---|---|
| `[x]` | Пройдено |
| `[~]` | В процессе |
| `[ ]` | Очередь этапа: изучаем в этой колее/этапе |
| `[→P1]`…`[→P5]` | Явно отложено: изучается в проекте N |
| `[skip]` | Вне скоупа Junior/Middle AI Engineer |
| `[covered]` | Покрыто в другой колее/этапе |

---

## 🟢 ЭТАП 0. Фундамент (4-5 недель)

### Колея 1: Python (Matthes) — ✅ АРХИВ
- **Ch.1-11 закрыты полностью** (158 скриптов). Детали: [`learning/01_python_core/README.md`](learning/01_python_core/README.md)

### Колея 2: ML-теория (Huyen DMLS, 11 глав) — 🎯 АКТИВНАЯ ЗОНА

**Глава 1: Overview of ML Systems**
- [x] 1.1 When to Use ML + Use Cases (эвристика «когда ML нужен, а когда нет» — шаги 160, 161)
- [x] 1.2 ML in Research vs Production (включая challenges — шаг 162)
- [x] 1.3 ML Systems vs Traditional Software (шаг 159)

**Глава 2: Introduction to ML Systems Design**
- [x] 2.1 Business and ML Objectives
- [x] 2.2 Requirements (reliability, scalability, maintainability, adaptability)
- [x] 2.3 Iterative Process
- [→P1] 2.4 Framing ML Problems + Types of ML Tasks
- [→P1] 2.5 Objective Functions
- [x] 2.6 Mind Versus Data

**Глава 3: Data Engineering Fundamentals**
- [ ] 3.1 Data Sources
- [→P2] 3.2 Data Formats (JSON, row/column-major, text/binary)
- [→P2] 3.3 Data Models (relational, NoSQL, structured/unstructured)
- [→P3] 3.4 Storage Engines and Processing (OLTP/OLAP, ETL)
- [→P3] 3.5 Modes of Dataflow (databases/services/real-time; batch vs stream)

**Глава 4: Training Data**
- [→P1] 4.1 Sampling (simple random, stratified, weighted, reservoir)
- [ ] 4.2 Labeling (hand, natural, lack of labels)
- [→P1] 4.3 Class Imbalance
- [→P1] 4.4 Data Augmentation (transformations, perturbation, synthesis)

**Глава 5: Feature Engineering**
- [ ] 5.1 Learned vs Engineered Features
- [→P1] 5.2 Common Operations (missing values, scaling, discretization, encoding, crossing)
- [→P1] 5.3 Data Leakage (причины, детекция)
- [→P1] 5.4 Engineering Good Features (importance, generalization)

**Глава 6: Model Development and Offline Evaluation**
- [→P1] 6.1 Model Development and Training
- [→P1] 6.2 Evaluating ML Models (метрики)
- [→P1] 6.3 Ensembles
- [→P2] 6.4 Experiment Tracking and Versioning
- [skip] 6.5 Distributed Training • [skip] 6.6 AutoML
- [→P1] 6.7 Baselines • [→P1] 6.8 Evaluation Methods (slice-based, invariance)

**Глава 7: Model Deployment and Prediction Service**
- [→P3] 7.1 Deployment Myths (4 мифа)
- [→P2] 7.2 Batch vs Online Prediction
- [→P5] 7.3 Model Compression (low-rank, distillation, pruning, quantization)
- [skip] 7.4 ML on Edge and in Browsers

**Глава 8: Data Distribution Shifts and Monitoring**
- [→P3] 8.1 Causes of ML System Failures
- [→P3] 8.2 Data Distribution Shifts (дрейф)
- [→P3] 8.3 Monitoring and Observability

**Глава 9: Continual Learning and Test in Production**
- [→P3] 9.1 Continual Learning (retraining)
- [→P3] 9.2 Test in Production (shadow, A/B, canary, bandits)

**Глава 10: Infrastructure and Tooling for MLOps**
- [→P3] 10.1 Storage and Compute; Public vs Private Cloud
- [→P2] 10.2 Development Environment + Containers
- [→P3] 10.3 Resource Management (cron, schedulers, orchestrators)
- [→P2] 10.4 Model Store (MLflow) • [skip] Feature Store • [→P4] Build vs Buy

**Глава 11: The Human Side of Machine Learning**
- [→P4] 11.1 User Experience
- [ ] 11.2 Team Structure (cross-functional, end-to-end DS)
- [→P5] 11.3 Responsible AI

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
- [ ] **Продвинутый Git** (ветки, PR, rebase) • [→P3] Git flow

---

## 🟡 ЭТАП 1. Wine Classifier (2-3 недели) — КОМПАКТ
> Детали раскрываются при входе в этап из `COURSE_PLAN_FULL.md`.

**Теория:**
- [ ] McMahon Ch.1: Intro to ML Eng (Taxonomy, Team, High-level design)
- [ ] McMahon Ch.2: ML Dev Process (Discover/Play/Develop/Deploy, CRISP-DM, CI/CD)

**Проект 1: Wine Classifier (Baseline)**
- **Теория [→P1]:** DMLS 2.4-2.5, 4.1-4.4, 5.2-5.4, 6.1-6.3/6.7-6.8
- **Практика:** sklearn, EDA, Feature Eng, LogisticRegression/RandomForest, метрики, pytest, структура `src/`.

---

## 🟠 ЭТАП 2. House Price Predictor (3-4 недели) — КОМПАКТ

**Теория:**
- [ ] McMahon Ch.3: Model Factory (Target, Loss, Features, Training, Drift [→P3], Pipelines) • [skip] Spark/AutoML
- [ ] McMahon Ch.4: Packaging (OOP/Functional, Poetry, Makefiles, Testing, Security)

**Проект 2: House Price Predictor (ML as a Service)**
- **Теория [→P2]:** DMLS 3.2-3.3, 6.4, 7.2, 10.2, 10.4
- **Практика:** California Housing, Pipelines, joblib, FastAPI, Docker, unit-тесты API.

---

## 🔵 ЭТАП 3. Sentiment Analyzer API (4-5 недель) — КОМПАКТ

**Теория:**
- [ ] Gift Ch.1: Intro to MLOps (DevOps, CI, Hierarchy of Needs)
- [covered] Gift Ch.2: MLOps Foundations (покрыто в Этапе 0)
- [ ] Gift Ch.3: Containers & Edge • [skip] Edge Devices
- [ ] Gift Ch.4: CD for ML (Packaging, IaC, Rollouts)
- [skip] Gift Ch.5: AutoML/KaizenML (Awareness only) • [ ] Kaizen concept
- [ ] Gift Ch.6: Monitoring & Logging (Observability, Drift)
- [ ] Gift Ch.7: MLOps for AWS (Focus) • [skip] Ch.8-9: Azure/GCP
- [skip] Gift Ch.10: Interoperability (ONNX) • [ ] Gift Ch.11: CLI Tools & Microservices
- [ ] Gift Ch.12: Case Studies & Best Practices • [ ] Apps: Portfolio, Project Mgmt
- [ ] McMahon Ch.5: Deployment Patterns (Microservices, Airflow) • [skip] ZenML/Kubeflow
- [skip] McMahon Ch.6: Scaling Up (Spark, K8s, Ray) • [ ] Designing at scale

**Проект 3: Sentiment Analyzer API (MLOps + Cloud)**
- **Теория [→P3]:** DMLS 3.4-3.5, 7.1, 8.1-8.3, 9.1-9.2; Gift 1.7, 3.4, 4.3-4.4, 6.2-6.5, 7.3-7.4, 11.1-11.4, 12.2-12.6
- **Практика:** TF-IDF + LogReg, FastAPI, Docker, GitHub Actions, AWS (EC2/Lambda), Evidently AI, резюме/LinkedIn.

---

## 🟣 ЭТАП 4. Foundation Models + RAG (5-6 недель) — КОМПАКТ

**Теория:**
- [ ] HF NLP Course (Tokenization, Fine-tuning, HF Hub)
- [ ] Huyen AI Ch.1: Rise of AI Eng (Use cases, Stack)
- [ ] Huyen AI Ch.2: Understanding Foundation Models (Training, Modeling, Sampling)
- [ ] Huyen AI Ch.3-4: Evaluation (Metrics, AI as Judge, Build vs Buy)
- [ ] Huyen AI Ch.5: Prompt Engineering (Best practices, Defensive)
- [ ] Huyen AI Ch.6: RAG and Agents (RAG focus) • [→P5] Agents & Memory
- [ ] Iusztin Ch.1: LLM Twin Concept (FTI pipelines, MVP)
- [ ] Iusztin Ch.2: Tooling (Poetry, ZenML, Comet, Qdrant) • [→P5] AWS SageMaker
- [ ] Iusztin Ch.3: Data Engineering (Crawlers, MongoDB, ODM)
- [ ] Iusztin Ch.4: RAG Feature Pipeline (Embeddings, Vector DBs, CDC)

**Проект 4: RAG-приложение для документов**
- **Теория [→P4]:** DMLS 10.4, 11.1; McMahon 7.1, 7.4-7.5
- **Практика:** Парсинг, чанкинг, ChromaDB, RAG-пайплайн, Streamlit/Gradio, Kaggle.

---

## 🔴 ЭТАП 5. LLM Twin (5-6 недель) — КОМПАКТ

**Теория:**
- [ ] Iusztin Ch.5: SFT (Instruction datasets, LoRA/QLoRA, Training params)
- [ ] Iusztin Ch.6: Preference Alignment (RLHF, DPO)
- [ ] Iusztin Ch.7: Evaluating LLMs (Ragas, ARES)
- [ ] Iusztin Ch.8: Inference Optimization (KV cache, Quantization) • [skip] Distributed
- [ ] Iusztin Ch.9: RAG Inference Pipeline (Advanced RAG, Reranking)
- [ ] Iusztin Ch.10: Deployment (FastAPI, Autoscaling)
- [ ] Iusztin Ch.11: MLOps/LLMOps (Guardrails, CI/CD/CT, Prompt monitoring)
- [ ] Iusztin App: MLOps Principles (6 принципов)
- [ ] Huyen AI Ch.7: Finetuning (Memory math, PEFT)
- [ ] Huyen AI Ch.8: Dataset Engineering (Curation, Synthesis)
- [ ] Huyen AI Ch.9: Inference Optimization (Service level)
- [ ] Huyen AI Ch.10: Architecture & User Feedback (Guardrails, Router, Caches)

**Проект 5: LLM Twin (Production-ready)**
- **Теория [→P5]:** DMLS 7.3, 9.2, 11.3; McMahon 7.2-7.3, 7.6-7.7; Huyen AI 6.5-6.6
- **Практика:** Google Colab, SFT/QLoRA, DPO, Guardrails, Docker, CometML, A/B, LeetCode/Mock interviews.

---

## 🎯 Общая длительность
**~12 месяцев (реалистичный горизонт)**