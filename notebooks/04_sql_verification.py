
import sqlite3
import pandas as pd

# Load Cleaned Data
df = pd.read_csv(r"d:\College\E-Commerce Sales Performance Project\data\cleaned\diwali_sales_cleaned.csv")

# Clean Column Names for SQL
# 1. Replace spaces with underscores
# 2. Remove special chars
# 3. deduplicate
new_cols = []
seen_cols = set()
for col in df.columns:
    # SQL-friendly name: replace spaces/dashes, strip, and make explicit
    clean_col = col.replace(' ', '_').replace('-', '_').strip()
    
    # Check for duplicates (case-insensitive for SQL safety)
    if clean_col.lower() in seen_cols:
        clean_col = f"{clean_col}_dup"
        # Handle triple duplicates if necessary
        n = 2
        while clean_col.lower() in seen_cols:
             clean_col = f"{clean_col.rsplit('_dup', 1)[0]}_dup{n}"
             n += 1
    
    seen_cols.add(clean_col.lower())
    new_cols.append(clean_col)

df.columns = new_cols
print(f"Columns for SQL: {df.columns.tolist()}")

# Create InMemory SQLite DB
conn = sqlite3.connect(':memory:')

# Write DataFrame to SQL Table
try:
    df.to_sql('sales_data', conn, index=False, if_exists='replace')
    print("Database initialized with sales_data table.")
except Exception as e:
    print(f"Error initializing DB: {e}")
    exit(1)

# Test Queries
queries = {
    "1. Total Revenue": """
        SELECT 
            SUM(Amount) as Total_Revenue,
            SUM(Orders) as Total_Orders
        FROM sales_data;
    """,
    "2. Top 5 States": """
        SELECT 
            State,
            SUM(Amount) as State_Revenue
        FROM sales_data
        GROUP BY State
        ORDER BY State_Revenue DESC
        LIMIT 5;
    """,
    "3. Festival Season Analysis": """
        SELECT 
            CASE 
                WHEN Month IN ('Oct', 'Nov') THEN 'Festival Season'
                ELSE 'Regular Season'
            END as Season,
            SUM(Amount) as Revenue
        FROM sales_data
        GROUP BY Season;
    """
}

print("\n--- RUNNING SQL CHECKS ---")
for title, sql in queries.items():
    print(f"\nQUERY: {title}")
    try:
        result = pd.read_sql(sql, conn)
        print(result)
    except Exception as e:
        print(f"Error executing query: {e}")

conn.close()
