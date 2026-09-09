-- Databricks notebook source
INSERT OVERWRITE case_study.gold.fact_daily_sales (
  sale_date, store_key, product_key,total_quantity_sold, total_revenue, total_estimated_margin
)
SELECT
  DATE(s.transaction_timestamp) AS sale_date,
  ds.store_key,
  dp.product_key,
  SUM(s.quantity) AS total_quantity_sold,
  SUM(s.total_sales_amount) AS total_revenue,
  SUM(s.estimated_margin) AS total_estimated_margin
FROM case_study.silver.clean_store_sales_updated s
JOIN case_study.gold.dim_store ds ON s.store_id = ds.store_id
JOIN case_study.gold.dim_product dp ON s.sku = dp.sku
GROUP BY sale_date, ds.store_key, dp.product_key;