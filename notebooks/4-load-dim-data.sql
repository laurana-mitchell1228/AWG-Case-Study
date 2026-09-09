-- Databricks notebook source
INSERT OVERWRITE case_study.gold.dim_product (sku, product_name, category, department)
SELECT DISTINCT sku, product_name, category, department
FROM case_study.silver.clean_product_catalog

-- COMMAND ----------

INSERT OVERWRITE case_study.gold.dim_store (store_id)
SELECT DISTINCT store_id
FROM case_study.silver.clean_store_sales;