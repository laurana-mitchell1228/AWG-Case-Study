# Databricks notebook source
# DBTITLE 1,Cell 1
import pandas as pd

# Clean the store sales dataset
df_sales_spark = spark.read.table("case_study.bronze.raw_store_sales")
df_prod_spark = spark.read.table("case_study.bronze.raw_product_catalog")
df_sales = df_sales_spark.toPandas()
df_prod = df_prod_spark.toPandas()

# Drop rows with missing SKU values
df_sales.dropna(subset=['sku'], inplace=True)

# Absolute value of quantity to ensure all values are positive
df_sales['quantity'] = abs(df_sales['quantity'])
# Could delete if desired instead
# df_sales = df_sales[df_sales["quantity"] >= 0]

# Convert transaction_timestamp to datetime format and standardize the format
df_sales['transaction_timestamp'] = pd.to_datetime(df_sales['transaction_timestamp'], format='mixed')
df_sales['transaction_timestamp'] = df_sales['transaction_timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')

# Clean the product catalog dataset
# Nothing here yet but could be added as needed in the future

df_sales_spark = spark.createDataFrame(df_sales)
df_sales_spark.writeTo("case_study.silver.clean_store_sales").createOrReplace()
df_prod_spark.writeTo("case_study.silver.clean_product_catalog").createOrReplace()


# Output the cleaned datasets to parquet files
pd.DataFrame(df_sales.to_dict('list')).to_parquet("/Workspace/Users/laurana.mitchell@gmail.com/AWG-Case-Study/Data/Silver/store_sales_clean.parquet")
pd.DataFrame(df_prod.to_dict('list')).to_parquet("/Workspace/Users/laurana.mitchell@gmail.com/AWG-Case-Study/Data/Silver/product_catalog_clean.parquet")