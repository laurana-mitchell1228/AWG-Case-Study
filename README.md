# AWG-Case-Study

## Architecture Diagram/Workflow
1. Bronze - Raw Data
    - load raw_store_sales.csv 
    - load raw_product_catalog.csv
2. Silver - Clean Data
    - raw_store_sales table is cleaned to remove null skus, normalize date format, and handle negative quantities.
    - raw_product_catalog table is currently not modified, but cleaning could be added for that as well during this step
    - total_sales_amount and estimated_margin are computed
    - clean_store_sales table is created
3. Gold - Business Ready Data
    - refresh dimension tables, dim_store and dim_product
    - refresh aggregated daily data in fact_daily_sales
    - connect to Power BI for reporting


## Orchestration
 - Set tasks in order each dependent on the previous
    1. 1-ingest-and-clean
    2. 2-calculate-new-metrics
    3. 3-load-dim-data
    4. 4-load-fact-data

 - Schedule job to run daily, sometime with lower traffic, late evening/early morning

 - Set up email alerts for job failures

## Monitoring & Support
1. Changes in schema
    - 
2. Late data
    - 
3. Major differences in data volume
    - 