-- Databricks notebook source
CREATE OR REPLACE TABLE case_study.cnfz.clean_store_sales_updated AS
SELECT transaction_id
,store_id
,s.sku
,quantity
,unit_price
,ROUND(s.quantity * s.unit_price,2) AS total_sales_amount
,ROUND((s.quantity * s.unit_price) - (s.quantity * p.standard_unit_cost),2) AS estimated_margin
,try_to_timestamp(transaction_timestamp, 'yyyy-MM-dd HH:mm:ss') AS transaction_timestamp
FROM case_study.cnfz.clean_store_sales s 
LEFT JOIN case_study.rawz.raw_product_catalog AS p ON s.sku = p.sku