# AWG-Case-Study

## Architecture Diagram/Workflow
1. Bronze
    - raw_store_sales.csv is loaded in to table
    - raw_product_catalog.csv is loaded in to table
2. Silver
    - raw_store_sales table is cleaned to remove null skus, normalize date format, and handle negative quantities.
    - raw_product_catalog table is currently not modified, but cleaning could be added for that as well during this step
    - total_sales_amount and estimated_margin are computed
    - clean_store_sales table is created
3. Gold
    - load product and sales data into dim_product, dim_store and fact_daily_sales
    - connect to Power BI for reporting


## Orchestration



## Monitoring & Support
1. Changes in schema
    - 
2. Major differences in data volume
    - 