-- Databricks notebook source
CREATE TABLE case_study.gold.fact_daily_sales (
    sale_date             DATE NOT NULL,
    store_key             BIGINT NOT NULL,
    product_key           BIGINT NOT NULL,
    total_quantity_sold   INTEGER NOT NULL,
    total_revenue         NUMERIC(12,2) NOT NULL,
    total_estimated_margin NUMERIC(12,2) NOT NULL,
    CONSTRAINT fk_fact_store
        FOREIGN KEY (store_key) REFERENCES case_study.pubz.dim_store(store_key),
    CONSTRAINT fk_fact_product
        FOREIGN KEY (product_key) REFERENCES case_study.pubz.dim_product(product_key)
);