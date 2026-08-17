# 📚 ПОЛНЫЙ ПЛАН КУРСА: ML/AI Engineer (Single Source of Truth)

## 🏷 Легенда маркеров (аудит скоупа)

| Маркер | Значение |
|---|---|
| `[x]` | Пройдено |
| `[~]` | В процессе |
| `[ ]` | Очередь этапа: изучаем в этой колее/этапе |
| `[→P1]`…`[→P5]` | Явно отложено: изучается в проекте N (обратная ссылка в секции проекта) |
| `[skip]` | Вне скоупа Junior/Middle AI Engineer (причина в скобках) |
| `[covered]` | Покрыто в другой колее/этапе (с указанием, где) |

**Правило аудита для Дмитрия:** каждая строка плана обязана иметь маркер. Строка без маркера — дыра; ты имеешь право требовать с ментора ответ.

---

## 🟢 ЭТАП 0. Фундамент: Python Core + ML-основы + математика (4-5 недель, интегрированный)

### Колея 1: Python (Matthes) — ✅ АРХИВ
- **Ch.1-11 закрыты полностью** (158 учебных скриптов, шаги 1-158; тесты по Главе 11)
- Концепции и связь с ML: `LEARNING_JOURNAL.md`
- Детальный чек-лист подглав: [`learning/01_python_core/README.md`](learning/01_python_core/README.md)

### Колея 2: ML-теория (Huyen DMLS, 11 глав)

**Huyen DMLS, Глава 1: Overview of ML Systems**
- [x] 1.1 When to Use ML + Use Cases (эвристика «когда ML нужен, а когда нет» — шаги 160, 161)
- [x] 1.2 ML in Research vs Production (включая challenges — шаг 162)
- [x] 1.3 ML Systems vs Traditional Software (шаг 159)

**Huyen DMLS, Глава 2: Introduction to ML Systems Design**
- [ ] 2.1 Business and ML Objectives
- [ ] 2.2 Requirements: reliability, scalability, maintainability, adaptability
- [ ] 2.3 Iterative Process
- [→P1] 2.4 Framing ML Problems + Types of ML Tasks
- [→P1] 2.5 Objective Functions
- [ ] 2.6 Mind Versus Data (спор «данные против алгоритмов»)

**Huyen DMLS, Глава 3: Data Engineering Fundamentals**
- [ ] 3.1 Data Sources
- [→P2] 3.2 Data Formats (JSON, row/column-major, text/binary)
- [→P2] 3.3 Data Models (relational, NoSQL, structured/unstructured)
- [→P3] 3.4 Storage Engines and Processing (OLTP/OLAP, ETL)
- [→P3] 3.5 Modes of Dataflow (databases/services/real-time; batch vs stream)

**Huyen DMLS, Глава 4: Training Data**
- [→P1] 4.1 Sampling (simple random, stratified, weighted, reservoir)
- [ ] 4.2 Labeling (hand, natural, lack of labels)
- [→P1] 4.3 Class Imbalance
- [→P1] 4.4 Data Augmentation (transformations, perturbation, synthesis)

**Huyen DMLS, Глава 5: Feature Engineering**
- [ ] 5.1 Learned vs Engineered Features
- [→P1] 5.2 Common Operations (missing values, scaling, discretization, encoding, crossing)
- [→P1] 5.3 Data Leakage (причины, детекция)
- [→P1] 5.4 Engineering Good Features (importance, generalization)

**Huyen DMLS, Глава 6: Model Development and Offline Evaluation**
- [→P1] 6.1 Model Development and Training
- [→P1] 6.2 Evaluating ML Models (метрики)
- [→P1] 6.3 Ensembles
- [→P2] 6.4 Experiment Tracking and Versioning
- [skip] 6.5 Distributed Training (Junior — один GPU/Colab)
- [skip] 6.6 AutoML (уровень осведомлённости; не навык Junior)
- [→P1] 6.7 Baselines
- [→P1] 6.8 Evaluation Methods (slice-based, invariance)

**Huyen DMLS, Глава 7: Model Deployment and Prediction Service**
- [→P3] 7.1 Deployment Myths (4 мифа)
- [→P2] 7.2 Batch vs Online Prediction (+ unification pipelines)
- [→P5] 7.3 Model Compression (low-rank, distillation, pruning, quantization — перекликается с QLoRA)
- [skip] 7.4 ML on Edge and in Browsers (вне нашего трека: сервер + Colab)

**Huyen DMLS, Глава 8: Data Distribution Shifts and Monitoring**
- [→P3] 8.1 Causes of ML System Failures (software + ML-specific)
- [→P3] 8.2 Data Distribution Shifts (типы, детекция, адресация — дрейф)
- [→P3] 8.3 Monitoring and Observability (ML-метрики, toolbox)

**Huyen DMLS, Глава 9: Continual Learning and Test in Production**
- [→P3] 9.1 Continual Learning (retraining, как часто обновлять)
- [→P3] 9.2 Test in Production (shadow, A/B, canary, bandits; A/B вернётся в P5)

**Huyen DMLS, Глава 10: Infrastructure and Tooling for MLOps**
- [→P3] 10.1 Storage and Compute; Public vs Private Cloud
- [→P2] 10.2 Development Environment + Containers (dev→prod)
- [→P3] 10.3 Resource Management (cron, schedulers, orchestrators)
- [→P2] 10.4 Model Store (MLflow) • [skip] Feature Store (не нужно Junior) • [→P4] Build vs Buy

**Huyen DMLS, Глава 11: The Human Side of Machine Learning**
- [→P4] 11.1 User Experience (consistency, smooth failing)
- [ ] 11.2 Team Structure (cross-functional, end-to-end DS — карьерный контекст)
- [→P5] 11.3 Responsible AI (фреймворк; перекликается с guardrails)

### Колея 3: Python для Data Science (Kaggle Learn + ментор)

**Kaggle Learn: Pandas (4 часа, интерактивно)**
- [ ] Создание и индексация DataFrame
- [ ] Выбор данных и фильтрация
- [ ] Сводные функции и groupby
- [ ] Работа с пропущенными значениями

**NumPy (ментор)**
- [ ] Основы массивов (ndarray)
- [ ] Индексация и срезы
- [ ] Broadcasting
- [ ] Линейная алгебра (dot product, матричные операции)

**Matplotlib и Seaborn (ментор)**
- [ ] Базовые графики (line, scatter, bar, hist)
- [ ] Визуализация распределений
- [ ] Heatmaps и correlation plots

### Колея 4: Математика для ML (3Blue1Brown + ментор)

**3Blue1Brown: Essence of Linear Algebra (YouTube, 15 видео, 3-4 часа)**
- [ ] Векторы и их геометрия
- [ ] Линейные комбинации и span
- [ ] Матрицы как линейные трансформации
- [ ] Determinant, inverse, rank
- [ ] Dot product и cross product

**Линейная алгебра (ментор, закрепление)**
- [ ] Векторы и операции
- [ ] Матрицы и трансформации
- [ ] Dot product и cosine similarity
- [ ] Нормы и расстояния

**Статистика (ментор)**
- [ ] Описательная статистика (mean, median, std, variance)
- [ ] Распределения (normal, binomial, poisson)
- [ ] Гипотезы и p-value
- [ ] Доверительные интервалы

**Теория вероятностей (ментор)**
- [ ] Базовые понятия (события, вероятность)
- [ ] Условная вероятность и теорема Байеса
- [ ] Математическое ожидание и дисперсия

### Колея 5: Инженерные основы (SQLZoo + ментор)

**SQLZoo (интерактивно, 5-6 часов)**
- [ ] SELECT, WHERE, ORDER BY
- [ ] JOIN и подзапросы
- [ ] GROUP BY и агрегатные функции
- [skip] Индексы и оптимизация (Junior достаточно базовых запросов; оптимизация — по потребности вакансии)

**HTTP и API (ментор)**
- [ ] REST API принципы
- [ ] HTTP методы (GET, POST, PUT, DELETE)
- [ ] Работа с JSON
- [ ] Библиотеки requests и httpx

**Linux и Bash (ментор)**
- [ ] Навигация (cd, ls, pwd)
- [ ] Работа с файлами (cat, grep, awk)
- [ ] Пайплайны и перенаправления
- [ ] Базовые скрипты

**Продвинутый Git (ментор)**
- [ ] Ветвление (branch, checkout, merge)
- [ ] Pull Requests и code review
- [ ] Rebase и разрешение конфликтов
- [→P3] Git flow и стратегии (командные практики; для соло достаточно branch + PR)

---

## 🟡 ЭТАП 1. Первый ML-проект: Wine Classifier (2-3 недели)

### Колея 1: ML-инженерия (McMahon Ch.1-2)

**McMahon, Глава 1: Introduction to ML Engineering**
- [ ] 1.1 Taxonomy of data disciplines (DS, MLE, MLOps, DE — карьерный контекст)
- [ ] 1.2 Working as an effective team
- [ ] 1.3 ML engineering in the real world
- [ ] 1.4 What does an ML solution look like?
- [ ] 1.5 Why Python?
- [ ] 1.6 High-level ML system design (3 примера: anomaly detection, forecasting API, classification pipeline)

**McMahon, Глава 2: The ML Development Process**
- [ ] 2.1 Setting up tools (+ AWS account)
- [ ] 2.2 Four steps: Discover → Play → Develop → Deploy
- [ ] 2.3 Comparing to CRISP-DM
- [ ] 2.4 Discover: user stories
- [ ] 2.5 Play
- [ ] 2.6 Develop: methodology, conda/pip, Poetry, Git strategies, model version control
- [ ] 2.7 Deploy: options, DevOps/MLOps, CI/CD (GitHub Actions), continuous testing/training

### Проект 1: Wine Classifier (Baseline)

**Что изучаем:**
- [ ] Matthes Ch.1-11 (полностью, архив)
- [ ] McMahon Ch.1-2 (настройка + процесс)

**Теория (обратные ссылки [→P1]):** DMLS 2.4-2.5, 4.1-4.4, 5.2-5.4, 6.1-6.3/6.7-6.8

**Практика:**
- [ ] Загрузка датасета Wine (sklearn.datasets)
- [ ] EDA с pandas и matplotlib
- [ ] Feature engineering (масштабирование, кодирование)
- [ ] Обучение моделей (Logistic Regression, Random Forest)
- [ ] Оценка метрик (accuracy, precision, recall, F1)
- [ ] Unit-тесты с pytest
- [ ] Структура проекта (src/, tests/, data/, notebooks/)

**Результат:** Рабочий классификатор вина с тестами и документацией.

---

## 🟠 ЭТАП 2. ML as a Service: House Price Predictor (3-4 недели)

### Колея 1: ML-инженерия (McMahon Ch.3-4)

**McMahon, Глава 3: From Model to Model Factory**
- [ ] 3.1 Defining the model factory
- [ ] 3.2 Learning about learning (target, loss functions)
- [ ] 3.3 Preparing the data
- [ ] 3.4 Engineering features (categorical, numerical)
- [ ] 3.5 Designing training system (train-run, train-persist, retraining)
- [→P3] 3.6 Drift detection (data/concept), diagnosing, remediating
- [ ] 3.7 Automating training + hyperparameter optimization (Hyperopt, Optuna) • [skip] AutoML (auto-sklearn/AutoKeras — уровень осведомлённости)
- [ ] 3.8 Persisting your models
- [ ] 3.9 Pipelines: Scikit-learn • [skip] Spark ML pipelines

**McMahon, Глава 4: Packaging Up**
- [ ] 4.1 Writing good Python (OOP/functional, standards)
- [ ] 4.2 Packaging your code (design, build)
- [ ] 4.3 Makefiles
- [ ] 4.4 Poetry
- [ ] 4.5 Testing, logging, error handling
- [ ] 4.6 Securing solutions (свой код + зависимости)

### Проект 2: House Price Predictor

**Что изучаем:**
- [ ] McMahon Ch.3-4

**Теория (обратные ссылки [→P2]):** DMLS 2.4, 3.2-3.3, 6.4, 7.2, 10.2, 10.4; McMahon 6.2, 8.1-8.2 (fastapi), 8.4

**Практика:**
- [ ] Загрузка датасета California Housing
- [ ] Feature engineering (категориальные, числовые признаки)
- [ ] Scikit-Learn Pipelines
- [ ] Model persistence (joblib)
- [ ] REST API с FastAPI
- [ ] Dockerfile и docker-compose
- [ ] Unit-тесты API

**Результат:** Полноценный ML-пайплайн с API и контейнеризацией.

---

## 🔵 ЭТАП 3. MLOps + Cloud: Sentiment Analyzer API (4-5 недель)

### Колея 1: MLOps и деплой (Gift Ch.1-12 + McMahon Ch.5-6)

**Gift, Глава 1: Introduction to MLOps**
- [ ] 1.1 Rise of the ML Engineer and MLOps
- [ ] 1.2 What Is MLOps?
- [ ] 1.3 DevOps and MLOps
- [ ] 1.4 An MLOps Hierarchy of Needs
- [ ] 1.5 Implementing DevOps
- [ ] 1.6 Configuring CI with GitHub Actions
- [→P3] 1.7 DataOps and Data Engineering • [→P3] Platform Automation • [→P3] MLOps

**Gift, Глава 2: MLOps Foundations** `[covered в Колеях 3-5 Этапа 0]`
- [covered] Bash and Linux (Колея 5: Linux и Bash)
- [covered] Python Crash Course, Math, Data Science (Колеи 3-4)
- [covered] Build MLOps Pipeline from Zero (практика в Проекте 3)

**Gift, Глава 3: MLOps for Containers and Edge Devices**
- [ ] 3.1 Containers (Runtime, Creating, Running, Best Practices)
- [ ] 3.2 Serving a Trained Model Over HTTP
- [skip] 3.3 Edge Devices (Coral, Azure Percept, TFHub, Porting Non-TPU) — вне скоупа
- [ ] 3.4 Containers for Managed ML Systems • [→P3] Build Once, Run Many Workflow

**Gift, Глава 4: Continuous Delivery for ML Models**
- [ ] 4.1 Packaging for ML Models
- [ ] 4.2 Infrastructure as Code for CD of ML Models
- [→P3] 4.3 Using Cloud Pipelines • [→P3] Controlled Rollout of Models (blue-green, canary)
- [→P3] 4.4 Testing Techniques for Model Deployment

**Gift, Глава 5: AutoML and KaizenML**
- [skip] 5.1 AutoML (MLOps Industrial Revolution) — уровень осведомлённости
- [ ] 5.2 Kaizen versus KaizenML (continuous improvement)
- [skip] 5.3 Feature Stores (не нужно Junior)
- [skip] 5.4 Apple/Google/Azure/AWS AutoML — уровень осведомлённости
- [skip] 5.5 Open Source AutoML (Ludwig, FLAML) — уровень осведомлённости
- [→P3] 5.6 Model Explainability

**Gift, Глава 6: Monitoring and Logging**
- [ ] 6.1 Observability for Cloud MLOps
- [ ] 6.2 Introduction to Logging • [→P3] Logging in Python • [→P3] Modifying Log Levels
- [→P3] 6.3 Logging Different Applications
- [→P3] 6.4 Monitoring and Observability • [→P3] Basics of Model Monitoring
- [→P3] 6.5 Monitoring Drift (AWS SageMaker, Azure ML)

**Gift, Глава 7: MLOps for AWS** (основной фокус)
- [ ] 7.1 Introduction to AWS
- [ ] 7.2 Getting Started with AWS Services
- [→P3] 7.3 MLOps on AWS • [→P3] MLOps Cookbook on AWS
- [→P3] 7.4 CLI Tools • [→P3] Flask Microservice
- [skip] 7.5 AWS Lambda Recipes (serverless покрыт McMahon 5)
- [ ] 7.6 Applying AWS ML to the Real World

**Gift, Глава 8: MLOps for Azure**
- [skip] 8.1-8.7 Azure CLI, SDK, Authentication, Compute, Deploying, Registering, Versioning, Pipelines, Designer, ML Lifecycle — вне фокуса курса (только AWS); по потребности вакансии

**Gift, Глава 9: MLOps for GCP**
- [skip] 9.1-9.5 GCP Overview, CI/CD, Kubernetes, Cloud Native DB, DataOps, Operationalizing ML — вне фокуса курса; по потребности вакансии

**Gift, Глава 10: Machine Learning Interoperability**
- [skip] 10.1-10.5 Why Interoperability, ONNX, ONNX Model Zoo, Convert PyTorch/TensorFlow to ONNX, Generic ONNX Checker, Deploy ONNX to Azure, Apple Core ML, Edge Integration — вне скоупа Junior

**Gift, Глава 11: Building MLOps CLI Tools and Microservices**
- [→P3] 11.1 Python Packaging • [→P3] The Requirements File
- [→P3] 11.2 Command Line Tools • [→P3] Creating a Dataset Linter • [→P3] Modularizing a CLI Tool
- [→P3] 11.3 Microservices • [→P3] Creating a Serverless Function • [→P3] Authenticating to Cloud Functions
- [→P3] 11.4 Building a Cloud-Based CLI • [→P3] ML CLI Workflows

**Gift, Глава 12: ML Engineering and MLOps Case Studies**
- [ ] 12.1 Unlikely Benefits of Ignorance in Building ML Models
- [→P3] 12.2 MLOps Projects (Sqor Sports, Mechanical Turk, Influencer Rank, Athlete Intelligence)
- [ ] 12.3 The Perfect Technique Versus the Real World
- [→P3] 12.4 Critical Challenges in MLOps • [→P3] Ethical and Unintended Consequences
- [ ] 12.5 Final Recommendations to Implement MLOps
- [→P3] 12.6 Data Governance and Cybersecurity • [→P3] MLOps Design Patterns

**Gift, Приложения**
- [skip] A. Key Terms (покрывается GLOSSARY.md)
- [→P3] B. Technology Certifications (AWS ML Specialty)
- [skip] C. Remote Work (не в скоупе)
- [skip] D. Think Like a VC (не в скоупе)
- [→P3] E. Building a Technical Portfolio for MLOps
- [skip] F-G. Case Studies and Resources (не в скоупе)
- [→P3] H. Technical Project Management

**McMahon, Глава 5: Deployment Patterns and Tools**
- [ ] 5.1 Architecting systems (building with principles)
- [ ] 5.2 Standard ML patterns (data lakes, microservices, event-based, batching)
- [ ] 5.3 Containerizing
- [ ] 5.4 Hosting microservice on AWS (ECR, ECS)
- [ ] 5.5 Building pipelines with Airflow (+ AWS, CI/CD for Airflow)
- [skip] 5.6 Advanced ML pipelines (ZenML, Kubeflow)

**McMahon, Глава 6: Scaling Up**
- [skip] 6.1 Scaling with Spark (big data; Junior — по потребности)
- [skip] 6.2 Serverless infrastructure (покрыто Gift 4.3)
- [skip] 6.3 Kubernetes (по потребности вакансии)
- [skip] 6.4 Scaling with Ray (по потребности вакансии)
- [ ] 6.5 Designing systems at scale (концептуальное резюме)

### Проект 3: Sentiment Analyzer API

**Что изучаем:**
- [ ] Gift Ch.1-12 (выборочно)
- [ ] McMahon Ch.5-6

**Теория (обратные ссылки [→P3]):** DMLS 3.4-3.5, 7.1, 8.1-8.3, 9.1-9.2, 10.1-10.3; Gift 1.7, 3.4, 4.3-4.4, 5.6, 6.2-6.5, 7.3-7.4, 11.1-11.4, 12.2-12.6; McMahon 3.6; Колея 5 «Git flow и стратегии»

**Практика:**
- [ ] Обучение модели классификации тональности (TF-IDF + LogisticRegression)
- [ ] Создание REST API с FastAPI
- [ ] Dockerfile и docker-compose
- [ ] GitHub Actions для CI/CD
- [ ] Деплой на AWS (EC2 или Lambda)
- [ ] Мониторинг с Evidently AI
- [ ] Unit-тесты API
- [ ] Начало подготовки к трудоустройству (резюме, LinkedIn, LeetCode)

**Результат:** Контейнеризованное ML-приложение с API, CI/CD и мониторингом.

---

## 🟣 ЭТАП 4. Foundation Models + RAG (5-6 недель)

### Колея 1: AI Engineering (Huyen AI Ch.1-6 + HF NLP Course + Iusztin Ch.1-4)

**Hugging Face NLP Course (официальный, 10-12 часов, встроить параллельно)**
- [ ] Tokenization и pipelines
- [ ] Fine-tuning pretrained models
- [ ] Training и evaluation
- [ ] Hugging Face Hub и model sharing

**Huyen AI, Глава 1: Introduction to Building AI Applications**
- [ ] 1.1 The Rise of AI Engineering (LM → LLM → Foundation Models → AI Engineering)
- [ ] 1.2 Foundation Model Use Cases (8 категорий: coding, writing, bots, aggregation...)
- [ ] 1.3 Planning AI Applications (use case evaluation, setting expectations, milestone planning, maintenance)
- [ ] 1.4 The AI Engineering Stack (3 слоя; AI Eng vs ML Eng vs Full-Stack)

**Huyen AI, Глава 2: Understanding Foundation Models**
- [ ] 2.1 Training Data (multilingual, domain-specific models)
- [ ] 2.2 Modeling (transformer architecture, model size, scaling)
- [ ] 2.3 Post-Training (supervised finetuning, preference finetuning — концепт сейчас, практика в P5)
- [ ] 2.4 Sampling (fundamentals, strategies, test time compute, structured outputs, probabilistic nature)

**Huyen AI, Глава 3: Evaluation Methodology**
- [ ] 3.1 Challenges of Evaluating Foundation Models
- [ ] 3.2 Language Modeling Metrics (entropy, cross entropy, perplexity)
- [ ] 3.3 Exact Evaluation (functional correctness, similarity, intro to embedding)
- [ ] 3.4 AI as a Judge (why, how, limitations, what models)
- [ ] 3.5 Ranking Models with Comparative Evaluation

**Huyen AI, Глава 4: Evaluate AI Systems**
- [ ] 4.1 Evaluation Criteria (domain-specific, generation, instruction-following, cost/latency)
- [ ] 4.2 Model Selection (workflow, build vs buy, public benchmarks)
- [ ] 4.3 Design Your Evaluation Pipeline (3 шага)

**Huyen AI, Глава 5: Prompt Engineering**
- [ ] 5.1 Introduction to Prompting (zero/few-shot, system/user prompt, context length/efficiency)
- [ ] 5.2 Best Practices (clear instructions, sufficient context, subtasks, think step-by-step, iterate, version prompts)
- [ ] 5.3 Defensive Prompt Engineering (jailbreaking, prompt injection, information extraction, defenses)

**Huyen AI, Глава 6: RAG and Agents**
- [ ] 6.1 RAG Architecture • 6.2 Retrieval Algorithms • 6.3 Retrieval Optimization • 6.4 RAG Beyond Texts *(Этап 4, P4)*
- [→P5] 6.5 Agents (overview, tools, planning, failure modes and evaluation) • 6.6 Memory *(Этап 5)*

**Iusztin, Глава 1: LLM Twin Concept and Architecture**
- [ ] 1.1 Understanding the LLM Twin concept (what, why matters, why not ChatGPT)
- [ ] 1.2 Planning the MVP (what is MVP, defining the LLM Twin MVP)
- [ ] 1.3 FTI pipelines (feature/training/inference architecture, benefits)
- [ ] 1.4 Designing the system architecture of the LLM Twin

**Iusztin, Глава 2: Tooling and Installation**
- [ ] 2.1 Python ecosystem and installation (Poetry, Poe the Poet)
- [ ] 2.2 MLOps/LLMOps tooling (HF model registry, ZenML, Comet ML, Opik)
- [ ] 2.3 Databases (MongoDB NoSQL, Qdrant vector)
- [→P5] 2.4 Preparing for AWS (SageMaker — опция; базовый трек: Colab + Docker)

**Iusztin, Глава 3: Data Engineering**
- [ ] 3.1 Designing the data collection pipeline
- [ ] 3.2 Implementing the data collection pipeline (ZenML, dispatcher, crawlers, ORM/ODM)
- [ ] 3.3 Gathering raw data into the data warehouse • 3.4 Troubleshooting

**Iusztin, Глава 4: RAG Feature Pipeline**
- [ ] 4.1 Understanding RAG (vanilla framework, hallucinations, old information)
- [ ] 4.2 Embeddings (what, why powerful, how created)
- [ ] 4.3 Vector DBs (index algorithms, DB operations)
- [ ] 4.4 Overview of advanced RAG (pre-retrieval, retrieval, post-retrieval)
- [ ] 4.5 RAG feature pipeline architecture (feature store, batch vs streaming, CDC)
- [ ] 4.6 Implementing the RAG feature pipeline (cleaning/chunking/embedding handlers)

### Проект 4: RAG-приложение для документов

**Что изучаем:**
- [ ] Huyen AI Ch.1-6
- [ ] HF NLP Course
- [ ] Iusztin Ch.1-4

**Теория (обратные ссылки [→P4]):** DMLS 10.4 (Build vs Buy), 11.1 (User Experience); McMahon 7.1, 7.4-7.5 (LLMs intro)

**Практика:**
- [ ] Сбор данных (парсинг PDF/веб-страниц)
- [ ] Чанкинг документов
- [ ] Создание embeddings (OpenAI или локальные модели)
- [ ] Векторная база данных (ChromaDB)
- [ ] RAG-пайплайн (retrieval + generation)
- [ ] Веб-интерфейс (Streamlit/Gradio)
- [ ] Оценка качества (AI as Judge)
- [ ] Kaggle: участие в 1-2 соревнованиях (Titanic, House Prices)

**Результат:** Чат-бот, отвечающий на вопросы по загруженным документам.

---

## 🔴 ЭТАП 5. Fine-tuning + Production-ready система: LLM Twin (5-6 недель)

### Колея 1: Fine-tuning и продакшен (Iusztin Ch.5-11 + Huyen AI Ch.7-10)

**Iusztin, Глава 5: Supervised Fine-Tuning**
- [ ] 5.1 Creating an instruction dataset (curation: filtering, dedup, decontamination, quality eval, augmentation)
- [ ] 5.2 Creating our own instruction dataset
- [ ] 5.3 SFT techniques (when to fine-tune, chat templates, PEFT: full/LoRA/QLoRA)
- [ ] 5.4 Training parameters (LR, batch size, epochs, optimizers, gradient checkpointing)
- [ ] 5.5 Fine-tuning in practice (на Google Colab)

**Iusztin, Глава 6: Fine-Tuning with Preference Alignment**
- [ ] 6.1 Understanding preference datasets (data, generation, evaluation)
- [ ] 6.2 Creating our own preference dataset
- [ ] 6.3 Preference alignment (RLHF, DPO)
- [ ] 6.4 Implementing DPO

**Iusztin, Глава 7: Evaluating LLMs**
- [ ] 7.1 Model evaluation (ML vs LLM eval, general/domain/task-specific)
- [ ] 7.2 RAG evaluation (Ragas, ARES)
- [ ] 7.3 Evaluating TwinLlama-3.1-8B (generating, evaluating, analyzing)

**Iusztin, Глава 8: Inference Optimization**
- [ ] 8.1 Model optimization strategies (KV cache, continuous batching, speculative decoding)
- [ ] 8.2 Model parallelism (data/pipeline/tensor — концептуально; Colab = 1 GPU)
- [ ] 8.3 Model quantization (GGUF/llama.cpp, GPTQ/EXL2)

**Iusztin, Глава 9: RAG Inference Pipeline**
- [ ] 9.1 Understanding the RAG inference pipeline
- [ ] 9.2 Advanced RAG techniques (query expansion, self-querying, filtered vector search, reranking)
- [ ] 9.3 Implementing the RAG inference pipeline

**Iusztin, Глава 10: Inference Pipeline Deployment**
- [ ] 10.1 Criteria for choosing deployment types (latency/throughput/data)
- [ ] 10.2 Inference deployment types (online/async/batch)
- [ ] 10.3 Monolithic vs microservices in model serving
- [ ] 10.4 Deploying the LLM Twin service (SageMaker опция / Docker базово; FastAPI business service)
- [ ] 10.5 Autoscaling capabilities

**Iusztin, Глава 11: MLOps and LLMOps**
- [ ] 11.1 The path to LLMOps (DevOps lifecycle, core concepts)
- [ ] 11.2 MLOps (core components, principles, ML vs MLOps engineering)
- [ ] 11.3 LLMOps (human feedback, guardrails, prompt monitoring)
- [ ] 11.4 Deploying the LLM Twin's pipelines to the cloud (MongoDB, Qdrant, ZenML, Docker, AWS)
- [ ] 11.5 Adding LLMOps (CI/CD/CT, GitHub Actions, prompt monitoring, alerting)

**Iusztin, Приложение: MLOps Principles**
- [ ] A.1 Automation • A.2 Versioning • A.3 Experiment tracking • A.4 Testing • A.5 Monitoring (logs, metrics, drifts, alerts) • A.6 Reproducibility

**Huyen AI, Глава 7: Finetuning**
- [ ] 7.1 Finetuning Overview
- [ ] 7.2 When to Finetune (reasons to / not to, finetuning vs RAG)
- [ ] 7.3 Memory Bottlenecks (backprop, memory math, numerical representations, quantization)
- [ ] 7.4 Finetuning Techniques (PEFT/LoRA, model merging, tactics)

**Huyen AI, Глава 8: Dataset Engineering**
- [ ] 8.1 Data Curation (quality, coverage, quantity, acquisition/annotation)
- [ ] 8.2 Data Augmentation and Synthesis (traditional, AI-powered, model distillation)
- [ ] 8.3 Data Processing (inspect, deduplicate, clean/filter, format)

**Huyen AI, Глава 9: Inference Optimization**
- [ ] 9.1 Understanding Inference Optimization (overview, performance metrics TTFT/TPOT, AI accelerators)
- [ ] 9.2 Model Optimization (quantization, distillation, parallelism) • 9.3 Inference Service Optimization (batching, KV-cache, speculative decoding)

**Huyen AI, Глава 10: AI Engineering Architecture and User Feedback**
- [ ] 10.1 Architecture: Step 1-5 (enhance context, guardrails, router/gateway, caches, agent patterns)
- [ ] 10.2 Monitoring and Observability • 10.3 AI Pipeline Orchestration
- [ ] 10.4 User Feedback (extracting conversational feedback, feedback design, limitations)

### Проект 5: LLM Twin (Production-ready)

**Что изучаем:**
- [ ] Iusztin Ch.5-11 + Приложение
- [ ] Huyen AI Ch.7-10

**Теория (обратные ссылки [→P5]):** DMLS 7.3 (model compression), 9.2 (test in production), 11.3 (responsible AI); McMahon 7.2-7.3, 7.6-7.7 (DL scaling, fine-tuning, LLMOps, PromptOps); Huyen AI 6.5-6.6 (agents + memory)

**Практика (на Google Colab):**
- [ ] Сбор данных (LinkedIn, GitHub, Medium)
- [ ] Создание instruction dataset
- [ ] Fine-tuning с LoRA/QLoRA
- [ ] RAG с ChromaDB
- [ ] Guardrails (hallucination, toxicity)
- [ ] Деплой (FastAPI + Docker)
- [ ] Мониторинг (CometML)
- [ ] A/B тестирование
- [ ] Kaggle: участие в соревнованиях
- [ ] Финальная подготовка к собеседованиям (LeetCode, System Design, Mock interviews)

**Результат:** Production-ready LLM-приложение для портфолио.

---

## 🎯 Общая длительность

**~12 месяцев (реалистичный горизонт)**