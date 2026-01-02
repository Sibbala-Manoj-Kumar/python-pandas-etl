# Customer Orders ETL Pipeline (Python + Pandas)

## Overview
This project implements an end-to-end ETL pipeline using Python and Pandas.
It processes raw customer and order data and produces an analytics-ready output.

## Business Objective
- Clean raw customer and order data
- Handle missing values
- Filter valid transactions
- Aggregate order amounts per customer
- Join customer master data
- Generate a final summarized dataset

## ETL Pipeline Diagram

![ETL Pipeline](assets/etl_pipeline.png)

## ETL Flow
1. Read customer and order CSV files
2. Clean and standardize column names
3. Handle missing values in order data
4. Filter completed orders
5. Aggregate total order amount per customer
6. Join customer data with aggregated orders
7. Write final output to CSV

## Project Structure
python_pandas_etl/
├── data/
│ ├── customers.csv
│ └── orders.csv
├── output/
│ └── customer_order_summary.csv
├── etl.py
├── final_etl.py
└── README.md

## Output
Final file:
Columns:
- customer_id
- customer_name
- city
- total_order_amount

## Technologies Used
- Python
- Pandas
