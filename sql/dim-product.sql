-- Databricks notebook source
CREATE TABLE case_study.gold.dim_product (
    product_key      BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    sku              VARCHAR(50) NOT NULL UNIQUE,
    product_name     VARCHAR(255),
    category         VARCHAR(100),
    department       VARCHAR(100)
);

-- COMMAND ----------

