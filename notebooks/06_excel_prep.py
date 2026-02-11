
import pandas as pd
import os

print("Preparing Excel Analysis file...")

# Load Cleaned Data
df = pd.read_csv(r"d:\College\E-Commerce Sales Performance Project\data\cleaned\diwali_sales_cleaned.csv")

# Initialize Excel Writer
output_path = r"d:\College\E-Commerce Sales Performance Project\excel\analysis.xlsx"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    # Sheet 1: Raw Data
    df.to_excel(writer, sheet_name='Raw Data', index=False)
    
    # Sheet 2: Summary (Initial Pivot Data)
    summary = df.describe(include='all').transpose()
    summary.to_excel(writer, sheet_name='Summary Stats')
    
    # Sheet 3: Pivot Analysis Placeholder
    # Create an empty dataframe with headers for clarity
    pivot_template = pd.DataFrame(columns=['Row Labels', 'Sum of Amount', 'Sum of Orders', 'Average Order Value'])
    pivot_template.to_excel(writer, sheet_name='Pivot Analysis', index=False)
    
    # Sheet 4: Charts Placeholder
    pd.DataFrame(['Insert Charts Here']).to_excel(writer, sheet_name='Charts', index=False, header=False)

print(f"Excel file created at: {output_path}")
print("Sheets created: Raw Data, Summary Stats, Pivot Analysis, Charts")
