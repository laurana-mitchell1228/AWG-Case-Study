-- Databricks notebook source
INSERT OVERWRITE case_study.pubz.dim_product (sku, product_name, category, department)
SELECT DISTINCT sku, product_name, category, department
FROM case_study.cnfz.clean_product_catalog

-- COMMAND ----------

INSERT OVERWRITE case_study.pubz.dim_store (store_id)
SELECT DISTINCT store_id
FROM case_study.cnfz.clean_store_sales;