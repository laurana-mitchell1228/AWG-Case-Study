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

                     ┌──────────────────────────┐
                     │        dim_product       │
                     │──────────────────────────│
                     │ product_key (PK)         │
                     │ sku                      │
                     │ product_name             │
                     │ category                 │
                     │ department               │
                     └──────────────┬───────────┘
                                    │
                                    │  
                                    │
        ┌───────────────────────────┴────────────────────────────┐
        │                    fact_daily_sales                    │
        │────────────────────────────────────────────────────────│
        │ sales_date                                             │
        │ store_key (FK)                                         │
        │ product_key (FK)                                       │
        │ total_quantity_sold                                    │
        │ total_revenue                                          │
        │ total_estimated_margin                                 │
        └───────────────────────────┬────────────────────────────┘
                                    │                           
                                    │           
                                    │                           
                     ┌──────────────┴──────────────┐   
                     │         dim_store           │  
                     │─────────────────────────────│   
                     │ store_key (PK)              │  
                     │ store_id                    │   
                     └─────────────────────────────┘   

## Orchestration
 - Set tasks in order each dependent on the previous
    1. 1-ingest-data
    2. 2-clean-and-standardize
    3. 3-calculate-new-metrics
    4. 4-load-dim-data
    5. 5-load-fact-data

 - Schedule job to run daily, sometime with lower traffic, late evening/early morning

 - Set up email alerts for job failures

## Monitoring & Support
1. Changes in schema
    - Enforce schema early in the bronze layer data so malformed data isn't passed on and job doesn't fail later
    - Quarantine files with schema anomolies
    - Log schema drift event
    - Validate schema before any silver processing, fail job and send alert if validation fails

2. Late data
    - Check for expected new files
    - Check for expected date in the files
    - Change job to run on file arrival instead of at scheduled time
    - Log when data was expected vs when it arrived
