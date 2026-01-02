import pandas as pd

# ============================================================
# STEP 1: READ INPUT DATA (CUSTOMERS & ORDERS)
# ============================================================

# Read customers data
customers_df = pd.read_csv("data/customers.csv")

# Read orders data
orders_df = pd.read_csv("data/orders.csv")


# ============================================================
# STEP 2: CLEAN COLUMN NAMES
# (Standardize columns for SQL / BigQuery compatibility)
# ============================================================

# Clean customers column names
customers_df.columns = (
    customers_df.columns
    .str.lower()
    .str.replace(" ", "_")
)

# Clean orders column names
orders_df.columns = (
    orders_df.columns
    .str.lower()
    .str.replace(" ", "_")
)

# Debug prints (comment when not needed)
# print("\n--- STEP 2: CLEANED COLUMN NAMES ---")
# print("Customers columns:", customers_df.columns.tolist())
# print("Orders columns:", orders_df.columns.tolist())


# ============================================================
# STEP 3: DATA QUALITY CHECK – MISSING VALUES
# ============================================================

# print("\n--- STEP 3: MISSING VALUE CHECK (BEFORE FIX) ---")
# print(orders_df.isna().sum())


# ============================================================
# STEP 4: HANDLE MISSING VALUES
# (Business rule: missing order_amount = 0)
# ============================================================

orders_df["order_amount"] = orders_df["order_amount"].fillna(0)

# print("\n--- STEP 4: MISSING VALUE CHECK (AFTER FIX) ---")
# print(orders_df.isna().sum())


# ============================================================
# STEP 5: FILTER VALID ORDERS
# (Keep only COMPLETED payments)
# ============================================================

# print("\n--- STEP 5: PAYMENT STATUS VALUES ---")
# print(orders_df["payment_status"].unique())

completed_orders_df = orders_df[
    orders_df["payment_status"] == "Completed"
]

# print("\n--- STEP 5: COMPLETED ORDERS ---")
# print(completed_orders_df)
# print("Completed orders shape:", completed_orders_df.shape)

# ============================================================
# step 6: GROUP BY & AGGREGATION - Total order amount per customer
# ============================================================
completed_agg_df = completed_orders_df.groupby('customer_id',as_index = False).agg(total_order_amount = ('order_amount','sum'))
# print('\n --- STEP 6: Total order amount per customer ---:\n',completed_agg_df)


# ============================================================
# STEP 7: JOIN CUSTOMERS WITH AGGREGATED ORDERS
# ============================================================

joined_df = completed_agg_df.merge(customers_df, on="customer_id",how="inner")
# print("\n --- STEP 7: joined customer and orders data-----")
# print(joined_df)

# ============================================================
# STEP 8: FINAL OUTPUT SELECTION (BUSINESS RELEVANT COLUMNS)
# ============================================================
final_output_df = joined_df[["customer_id","customer_name","city","total_order_amount"]]
# print("\n --- STEP 8: FINAL OUTPUT DATA -----")
# print(final_output_df)

#===========================================================
# STEP 9: SAVE FINAL OUTPUT TO CSV
# ============================================================
final_output_df.to_csv("output/customer_order_summary.csv",index=False)
print("\n --- STEP 9: FINAL OUTPUT SAVED TO 'output/customer_order_summary.csv' -----")