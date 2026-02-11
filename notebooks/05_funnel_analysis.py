
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Ensure images directory exists
os.makedirs(r"d:\College\E-Commerce Sales Performance Project\images", exist_ok=True)

# 1. Load Data
print("Loading data for Funnel Analysis...")
df = pd.read_csv(r"d:\College\E-Commerce Sales Performance Project\data\cleaned\diwali_sales_cleaned.csv")

# 2. Define Funnel Stages (Customer Segment Funnel)
# Stage 1: All Customers (Total Unique User_IDs)
# Stage 2: Repeat Customers (Orders > 1)
# Stage 3: Loyal Customers (Orders > 3)
# Stage 4: VIP Customers (Top 10% by Revenue)

# Group by Customer
cust_agg = df.groupby('User_ID').agg({
    'Orders': 'count', # Count of transactions/orders
    'Amount': 'sum',
    'State': 'first', # Assume customer region
    'Gender': 'first'
}).reset_index()

# Stage 1: Total
total_customers = cust_agg.shape[0]

# Stage 2: Repeat
repeat_customers = cust_agg[cust_agg['Orders'] > 1].shape[0]

# Stage 3: Loyal
loyal_customers = cust_agg[cust_agg['Orders'] > 3].shape[0]

# Stage 4: VIP (Top 10% Revenue)
revenue_threshold = cust_agg['Amount'].quantile(0.90)
vip_customers = cust_agg[cust_agg['Amount'] >= revenue_threshold].shape[0]

funnel_data = dict(
    stages=['Total Customers', 'Repeat Customers (>1 Order)', 'Loyal Customers (>3 Orders)', 'VIP Customers (Top 10%)'],
    values=[total_customers, repeat_customers, loyal_customers, vip_customers]
)

print("\nFUNNEL METRICS:")
print(f"Total: {total_customers}")
print(f"Repeat: {repeat_customers} (Conversion: {repeat_customers/total_customers:.1%})")
print(f"Loyal: {loyal_customers} (Conversion: {loyal_customers/total_customers:.1%})")
print(f"VIP: {vip_customers} (Conversion: {vip_customers/total_customers:.1%})")

# 3. Visualization

# 3.1 Funnel Chart
fig = go.Figure(go.Funnel(
    y = funnel_data['stages'],
    x = funnel_data['values'],
    textposition = "inside",
    textinfo = "value+percent initial",
    opacity = 0.65, 
    marker = {"color": ["deepskyblue", "lightsalmon", "tan", "teal"]}
))
fig.update_layout(title_text="Customer Segmentation Funnel")

# Save as static image
output_path = r"d:\College\E-Commerce Sales Performance Project\images\11_customer_funnel.png"
fig.write_image(output_path)
print(f"Saved funnel chart to: {output_path}")

# 3.2 Regional Funnel Comparison (Top 3 States)
top_states = cust_agg['State'].value_counts().head(3).index.tolist()

fig2 = go.Figure()

for state in top_states:
    state_cust = cust_agg[cust_agg['State'] == state]
    
    s_total = state_cust.shape[0]
    s_repeat = state_cust[state_cust['Orders'] > 1].shape[0]
    s_loyal = state_cust[state_cust['Orders'] > 3].shape[0]
    
    # VIP threshold specific to state or global? Let's use global to see high value concentration
    s_vip = state_cust[state_cust['Amount'] >= revenue_threshold].shape[0]
    
    fig2.add_trace(go.Funnel(
        name = state,
        y = funnel_data['stages'],
        x = [s_total, s_repeat, s_loyal, s_vip],
        textinfo = "value+percent initial"
    ))

fig2.update_layout(title_text="Funnel Comparison by Top 3 States")
output_path2 = r"d:\College\E-Commerce Sales Performance Project\images\12_regional_funnel_comparison.png"
fig2.write_image(output_path2)
print(f"Saved regional funnel comparison to: {output_path2}")
