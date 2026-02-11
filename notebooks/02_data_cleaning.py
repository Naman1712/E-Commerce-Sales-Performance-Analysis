
import pandas as pd
import numpy as np
import os

# 1. Load Raw Data
print("Loading raw data...")
try:
    df = pd.read_csv(r"d:\College\E-Commerce Sales Performance Project\data\raw\Diwali Sales Data.csv", encoding='latin1')
except FileNotFoundError:
    print("Error: Raw data file not found.")
    exit(1)

print(f"Original Shape: {df.shape}")

# 2. Data Cleaning
print("\nCleaning data...")

# Drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True, errors='ignore')

# Handle Missing Values
print(f"Missing Amount values before drop: {df['Amount'].isnull().sum()}")
df.dropna(subset=['Amount'], inplace=True)
print(f"Shape after dropping missing Amount: {df.shape}")

# Drop Duplicates
df.drop_duplicates(inplace=True)
print(f"Shape after dropping duplicates: {df.shape}")

# Type Conversion
df['Amount'] = df['Amount'].astype('int') # Amount to int
df['User_ID'] = df['User_ID'].astype('string')

# Standardize Text
df['State'] = df['State'].str.strip()
df['Zone'] = df['Zone'].str.strip()
df['Occupation'] = df['Occupation'].str.strip()
df['Product_Category'] = df['Product_Category'].str.strip()

# 3. Feature Engineering & Date Simulation
print("\nGenerating synthetic dates for 2022...")

# Set random seed for reproducibility
np.random.seed(42)

# Define date range for 2022
start_date = pd.to_datetime('2022-01-01')
end_date = pd.to_datetime('2022-12-31')
days_range = (end_date - start_date).days

# Create a probability distribution for dates
# Higher probability during Festival Season (Oct-Nov for Diwali)
# Diwali 2022 was Oct 24
days = np.arange(days_range + 1)
probs = np.ones(len(days))

# Boost Oct/Nov weights (approx days 270 to 330)
probs[270:335] = 3.0  # 3x more likely to buy during festival season
probs = probs / probs.sum()

# Generate random days based on distribution
random_days = np.random.choice(days, size=len(df), p=probs)
df['Order_Date'] = start_date + pd.to_timedelta(random_days, unit='d')

# Extract Time Features
df['Year'] = df['Order_Date'].dt.year
df['Month'] = df['Order_Date'].dt.strftime('%b') # Jan, Feb...
df['Month_Num'] = df['Order_Date'].dt.month
df['Day_of_Week'] = df['Order_Date'].dt.day_name()
df['Quarter'] = df['Order_Date'].dt.to_period('Q').astype(str)

# 4. Additional Business Features
# Age Group Standardization (if needed - currently looks okay like '26-35')
# Order Value Category
def classify_order_value(amount):
    if amount < 1000: return 'Low'
    elif amount < 5000: return 'Medium'
    elif amount < 10000: return 'High'
    else: return 'Very High'

df['Order_Value_Category'] = df['Amount'].apply(classify_order_value)

# 5. Export Cleaned Data
output_path = r"d:\College\E-Commerce Sales Performance Project\data\cleaned\diwali_sales_cleaned.csv"
df.to_csv(output_path, index=False)
print(f"\nCleaned data saved to: {output_path}")
print(f"Final Shape: {df.shape}")
print(df.head())
