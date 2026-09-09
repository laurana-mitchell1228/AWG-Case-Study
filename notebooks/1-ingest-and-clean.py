# Databricks notebook source
# Import necessary libraries
import pandas as pd

# Ingest both datasets
df_prod = pd.read_csv('/Workspace/Users/laurana.mitchell@gmail.com/AWG-Case-Study/Data/Bronze(rawz)/raw_product_catalog.csv')
df_sales = pd.read_csv('/Workspace/Users/laurana.mitchell@gmail.com/AWG-Case-Study/Data/Bronze(rawz)/raw_store_sales.csv')


# Clean the store sales dataset

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
df_sales_spark.writeTo("case_study.cnfz.clean_store_sales").createOrReplace()
df_prod_spark = spark.createDataFrame(df_prod)
df_prod_spark.writeTo("case_study.cnfz.clean_product_catalog").createOrReplace()

# Output the cleaned datasets to parquet files
df_sales.to_parquet("/Workspace/Users/laurana.mitchell@gmail.com/AWG-Case-Study/Data/Silver(cnfz)/store_sales_clean.parquet")
df_prod.to_parquet("/Workspace/Users/laurana.mitchell@gmail.com/AWG-Case-Study/Data/Silver(cnfz)/product_catalog_clean.parquet")