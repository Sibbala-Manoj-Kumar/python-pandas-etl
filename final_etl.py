import pandas as pd

# ============================================================
# STEP 1: READ INPUT DATA
# ============================================================
def read_data():
    customers = pd.read_csv("data/customers.csv")
    orders = pd.read_csv("data/orders.csv")
    return customers, orders

# ============================================================
# STEP 2: CLEAN COLUMN NAMES
# ============================================================
def clean_columns(df):
    df.columns = df.columns.str.lower().str.replace(' ','_')
    return df

# ============================================================
# STEP 3 & 4: PREPROCESS ORDERS
# - Handle missing values
# - Filter completed payments
# ============================================================
def preprocess_orders(orders):
    orders['order_amount'] = orders['order_amount'].fillna(0)
    completed_orders = orders[orders['payment_status'] == 'Completed']
    return completed_orders

# ============================================================
# STEP 6: AGGREGATE DATA
# ============================================================
def aggregate_orders(orders):
    aggregated = (orders.groupby('customer_id',as_index = False).agg(total_order_amount = ('order_amount','sum')))
    return aggregated

# ============================================================
# STEP 7: JOIN DATASETS
# ============================================================
def join_datasets(customers, aggregated_orders):
    joined = aggregated_orders.merge(customers, on='customer_id',how = 'inner')
    return joined

# ============================================================
# STEP 8: FINAL OUTPUT SELECTION
# ============================================================
def select_final_columns(joined_df):
    final_df = joined_df[['customer_id', 'customer_name','city', 'total_order_amount']]
    return final_df

# ============================================================
# STEP 9: WRITE OUTPUT
# ============================================================
def write_output(df):
    df.to_csv('output/customer_order_summary.csv',index = False)

# ============================================================
# MAIN PIPELINE
# ============================================================
def main():
    customers, orders = read_data()
    
    customers = clean_columns(customers)
    orders = clean_columns(orders)

    completed_orders = preprocess_orders(orders)
    aggregated_orders = aggregate_orders(completed_orders)

    joined_df = join_datasets(customers, aggregated_orders)
    final_output_df = select_final_columns(joined_df)

    write_output(final_output_df)

    print('ETL Pipeline executed successfully!')

if __name__ == "__main__":
    main()
