-- Databricks notebook source
CREATE TABLE case_study.gold.dim_store (
    store_key   BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    store_id    VARCHAR(50) NOT NULL UNIQUE
);
