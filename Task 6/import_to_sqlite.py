import pandas as pd
import sqlite3

# Load the cleaned CSV
df = pd.read_csv("Chocolate_Sales_Cleaned.csv")

# Connect to SQLite (creates chocolate_sales.db if it doesn't exist)
conn = sqlite3.connect("chocolate_sales.db")

# Write data to a table named chocolate_sales
df.to_sql("chocolate_sales", conn, if_exists="replace", index=False)

conn.close()

print("Data imported successfully!")
