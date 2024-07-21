from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit


def solution():
    # Создаем Spark сессию
    spark = SparkSession.builder \
        .appName("ProductCategoryPairs") \
        .getOrCreate()

    # Пример данных
    products_data = [
        (1, "Product A"),
        (2, "Product B"),
        (3, "Product C")
    ]

    categories_data = [
        (1, "Category X"),
        (2, "Category Y")
    ]

    product_category_relations_data = [
        (1, 1),
        (2, 1),
        (2, 2)
    ]

    # Создаем датафреймы
    products_df = spark.createDataFrame(
        products_data, ["product_id", "product_name"])
    categories_df = spark.createDataFrame(
        categories_data, ["category_id", "category_name"])
    product_category_relations_df = spark.createDataFrame(
        product_category_relations_data, ["product_id", "category_id"])

    # Выполняем левое соединение для получения всех пар «Имя продукта – Имя категории»
    product_category_pairs_df = products_df.join(
        product_category_relations_df,
        on="product_id",
        how="left"
    ).join(
        categories_df,
        on="category_id",
        how="left"
    ).select(
        col("product_name"),
        col("category_name")
    )

    # Отбираем пары «Имя продукта – Имя категории»
    product_category_pairs_df.show()

    # Находим продукты без категорий
    products_without_categories_df = products_df.join(
        product_category_relations_df,
        on="product_id",
        how="left"
    ).where(
        col("category_id").isNull()
    ).select(
        col("product_name")
    )

    # Выводим имена продуктов без категорий
    products_without_categories_df.show()
