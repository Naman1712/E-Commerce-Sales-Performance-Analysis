
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Ensure images directory exists
os.makedirs(r"d:\College\E-Commerce Sales Performance Project\images", exist_ok=True)

# 1. Load Cleaned Data
print("Loading cleaned data...")
df = pd.read_csv(r"d:\College\E-Commerce Sales Performance Project\data\cleaned\diwali_sales_cleaned.csv")
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

print(f"Data Loaded: {df.shape}")

# Function to save plot
def save_plot(filename):
    path = os.path.join(r"d:\College\E-Commerce Sales Performance Project\images", filename)
    plt.tight_layout()
    plt.savefig(path, dpi=300)
    print(f"Saved: {filename}")
    plt.close()

# --- 3.1 UNIVARIATE ANALYSIS ---

# Distribution of Order Amounts
plt.figure(figsize=(10, 6))
sns.histplot(df['Amount'], bins=30, kde=True, color='skyblue')
plt.title('Distribution of Order Amounts')
plt.xlabel('Amount')
save_plot('01_amount_distribution.png')

# Count of Orders by Gender
plt.figure(figsize=(8, 5))
ax = sns.countplot(data=df, x='Gender', palette='pastel')
for container in ax.containers:
    ax.bar_label(container)
plt.title('Orders by Gender')
save_plot('02_orders_by_gender.png')

# Count of Orders by Age Group
plt.figure(figsize=(10, 6))
order_age = df['Age Group'].value_counts().index
sns.countplot(data=df, x='Age Group', order=order_age, palette='muted')
plt.title('Orders by Age Group')
save_plot('03_orders_by_age_group.png')

# --- 3.2 BIVARIATE ANALYSIS ---

# Total Amount by Gender
plt.figure(figsize=(8, 5))
sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Gender', y='Amount', data=sales_gen, palette='pastel')
plt.title('Total Revenue by Gender')
save_plot('04_revenue_by_gender.png')

# Total Amount by State (Top 10)
plt.figure(figsize=(15, 8))
sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.barplot(x='State', y='Amount', data=sales_state, palette='viridis')
plt.title('Top 10 States by Revenue')
plt.xticks(rotation=45)
save_plot('05_top_10_states_revenue.png')

# Marital Status vs Amount
plt.figure(figsize=(8, 5))
sales_marital = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Marital_Status', y='Amount', hue='Gender', data=sales_marital, palette='Set2')
plt.title('Revenue by Marital Status & Gender')
save_plot('06_revenue_marital_status.png')

# --- 3.3 MULTIVARIATE / TIME SERIES ---

# Monthly Sales Trend
plt.figure(figsize=(12, 6))
monthly_sales = df.groupby('Month_Num')['Amount'].sum()
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sns.lineplot(x=months, y=monthly_sales.values, marker='o', linewidth=2.5, color='orange')
plt.title('Monthly Sales Trend (Simulated 2022)')
plt.ylabel('Total Revenue')
save_plot('07_monthly_sales_trend.png')

# Weekly Sales Trend
plt.figure(figsize=(10, 6))
order_dow = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sns.countplot(data=df, x='Day_of_Week', order=order_dow, palette='cividis')
plt.title('Orders by Day of Week')
save_plot('08_orders_by_day_of_week.png')

# --- 3.4 FESTIVAL ANALYSIS (DIWALI) ---

# Define Festival Period (Oct & Nov)
df['Is_Festival'] = df['Month'].isin(['Oct', 'Nov'])
festival_sales = df.groupby('Is_Festival')['Amount'].sum()

plt.figure(figsize=(8, 6))
colors = ['lightgray', 'gold']
plt.pie(festival_sales, labels=['Non-Festival', 'Festival Season'], autopct='%1.1f%%', colors=colors, startangle=140, explode=(0, 0.1))
plt.title('Festival vs Non-Festival Revenue Share')
save_plot('09_festival_revenue_share.png')

# Top Categories during Festival
festival_df = df[df['Is_Festival'] == True]
top_fest_cats = festival_df.groupby('Product_Category')['Amount'].sum().sort_values(ascending=False).head(5)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_fest_cats.values, y=top_fest_cats.index, palette='magma')
plt.title('Top 5 Product Categories during Festival Season')
plt.xlabel('Revenue')
save_plot('10_top_festival_categories.png')

print("EDA Completed. Images saved to 'images/' directory.")
