"""
Микро-шаг 173: Системы хранения и обработки (Storage Engines, OLTP/OLAP, ETL).
Демонстрирует разницу между операционными (OLTP) и аналитическими (OLAP)
базами данных, а также процесс ETL для подготовки данных.
В ML это используется для извлечения сырых данных из операционных систем
и их подготовки в аналитических хранилищах перед обучением модели.
"""

# ── OLTP: Online Transaction Processing ──
# Быстрая запись отдельных транзакций, нормализованные данные
print("OLTP (Online Transaction Processing):")
print("  Цель: быстрая запись операционных данных (транзакций).")

oltp_orders: list[dict[str, str | int | float]] = [
    {"order_id": 101, "user_id": 1, "amount": 50.00},
    {"order_id": 102, "user_id": 2, "amount": 75.50},
    {"order_id": 103, "user_id": 1, "amount": 120.00},
]

print("  Пример таблицы orders:")
for order in oltp_orders:
    print(f"    {order}")

# ── OLAP: Online Analytical Processing ──
# Быстрое чтение агрегированных данных, денормализованные витрины
print("\nOLAP (Online Analytical Processing):")
print("  Цель: быстрый анализ больших объёмов данных.")

olap_user_stats: list[dict[str, str | int | float]] = [
    {"user_id": 1, "total_orders": 2, "total_spent": 170.00, "city": "Moscow"},
    {"user_id": 2, "total_orders": 1, "total_spent": 75.50, "city": "Berlin"},
]

print("  Пример аналитической витрины user_stats:")
for stat in olap_user_stats:
    print(f"    {stat}")

# ── ETL: Extract, Transform, Load ──
print("\nПроцесс ETL (Extract, Transform, Load):")

# Extract: извлекаем данные из OLTP
print("  1. Extract (Извлечение):")
print("     Берём сырые данные из OLTP (orders, users).")

# Transform: преобразуем данные для аналитики
print("  2. Transform (Преобразование):")
print("     Агрегируем заказы по пользователям (GROUP BY user_id).")

def transform_orders(orders: list[dict]) -> dict[int, dict]:
    """Агрегирует заказы по user_id."""
    aggregated: dict[int, dict] = {}
    for order in orders:
        user_id: int = order["user_id"]
        if user_id not in aggregated:
            aggregated[user_id] = {
                "user_id": user_id,
                "total_orders": 0,
                "total_spent": 0.0
            }
        aggregated[user_id]["total_orders"] += 1
        aggregated[user_id]["total_spent"] += order["amount"]
    return aggregated

transformed_data = transform_orders(oltp_orders)
print(f"     Результат трансформации: {list(transformed_data.values())}")

# Load: загружаем в OLAP
print("  3. Load (Загрузка):")
print("     Сохраняем агрегированные данные в OLAP (user_stats).")

# ── Сравнение OLTP и OLAP ──
print("\nСравнение OLTP и OLAP:")

comparison: list[dict[str, str]] = [
    {
        "характеристика": "Основная операция",
        "oltp": "INSERT, UPDATE, DELETE (запись)",
        "olap": "SELECT (чтение, аналитика)",
    },
    {
        "характеристика": "Объём данных",
        "oltp": "Текущие данные (мегабайты/гигабайты)",
        "olap": "Исторические данные (терабайты)",
    },
    {
        "характеристика": "Структура",
        "oltp": "Нормализованная (много таблиц, JOIN)",
        "olap": "Денормализованная (звезда, снежинка)",
    },
    {
        "характеристика": "Скорость",
        "oltp": "Быстрая запись, медленная сложная аналитика",
        "olap": "Медленная загрузка, быстрая сложная аналитика",
    },
]

for row in comparison:
    print(f"  {row['характеристика']}:")
    print(f"    OLTP: {row['oltp']}")
    print(f"    OLAP: {row['olap']}")

# ── Связь с ML ──
print("\nСвязь с ML:")
print("  OLTP (PostgreSQL, MySQL):")
print("    -> где живут сырые данные приложения")
print("  ETL (Airflow, dbt, Spark):")
print("    -> как данные попадают в хранилище и очищаются")
print("  OLAP (ClickHouse, BigQuery, Snowflake):")
print("    -> откуда ML-инженер берёт датасеты для обучения")
print("    -> где данные уже агрегированы и готовы для pandas/sklearn")