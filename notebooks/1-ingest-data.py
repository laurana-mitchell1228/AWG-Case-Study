# Databricks notebook source
import pandas as pd

# Ingest both datasets
df_prod = pd.read_csv('/Workspace/Users/laurana.mitchell@gmail.com/AWG-Case-Study/Data/Bronze/raw_product_catalog.csv')
df_sales = pd.read_csv('/Workspace/Users/laurana.mitchell@gmail.com/AWG-Case-Study/Data/Bronze/raw_store_sales.csv')

# Create sales table in bronze 
df_sales_spark = spark.createDataFrame(df_sales)
df_sales_spark.writeTo("case_study.bronze.raw_store_sales").createOrReplace()

# Create product table in bronze
df_prod_spark = spark.createDataFrame(df_prod)
df_prod_spark.writeTo("case_study.bronze.raw_product_catalog").createOrReplace()