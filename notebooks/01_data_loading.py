
import kagglehub
import pandas as pd
import os
import shutil

# 1. Download Dataset
print("Downloading dataset...")
path = kagglehub.dataset_download("umairabbasi6/diwali-sales-data-e-commerce-dataset")
print("Dataset downloaded to:", path)

# 2. Find the CSV file
csv_file = None
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".csv"):
            csv_file = os.path.join(root, file)
            break

if not csv_file:
    print("Error: No CSV file found in the downloaded dataset.")
    exit(1)

print(f"Found CSV file: {csv_file}")

# 3. Load Data
try:
    df = pd.read_csv(csv_file, encoding='latin1') # 'latin1' often needed for older datasets
except UnicodeDecodeError:
    df = pd.read_csv(csv_file)

# Save RAW data to project folder
raw_data_path = r"d:\College\E-Commerce Sales Performance Project\data\raw\Diwali Sales Data.csv"
shutil.copy(csv_file, raw_data_path)
print(f"Copied raw data to: {raw_data_path}")

# 4. Inspect Data
print("\n" + "="*50)
print("FIRST 10 ROWS")
print("="*50)
print(df.head(10))

print("\n" + "="*50)
print("DATASET SHAPE")
print("="*50)
print(df.shape)

print("\n" + "="*50)
print("COLUMN INFO")
print("="*50)
print(df.info())

print("\n" + "="*50)
print("MISSING VALUES")
print("="*50)
print(df.isnull().sum())

print("\n" + "="*50)
print("BASIC STATISTICS")
print("="*50)
print(df.describe(include='all'))

print("\n" + "="*50)
print("UNIQUE VALUES (Categorical Columns)")
print("="*50)
for col in df.select_dtypes(include=['object']).columns:
    print(f"\nColumn: {col}")
    print(df[col].unique()[:20]) # Show first 20 unique values
    print(f"Count: {df[col].nunique()}")
