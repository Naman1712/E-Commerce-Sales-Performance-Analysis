-- 1. Total Revenue, Total Orders, Average Order Value
SELECT 
    SUM(Amount) as Total_Revenue,
    SUM(Orders) as Total_Orders,
    AVG(Amount/Orders) as Avg_Order_Value
FROM sales_data;

-- 2. Monthly Sales Trends (Revenue by Month)
SELECT 
    Month,
    SUM(Amount) as Monthly_Revenue
FROM sales_data
GROUP BY Month
ORDER BY Monthly_Revenue DESC;

-- 3. Top 10 Products by Revenue
SELECT 
    Product_ID,
    Product_Category,
    SUM(Amount) as Product_Revenue
FROM sales_data
GROUP BY Product_ID, Product_Category
ORDER BY Product_Revenue DESC
LIMIT 10;

-- 4. Category-wise Performance
SELECT 
    Product_Category,
    SUM(Amount) as Revenue,
    SUM(Orders) as Total_Orders
FROM sales_data
GROUP BY Product_Category
ORDER BY Revenue DESC;

-- 5. State-wise Revenue Ranking
SELECT 
    State,
    SUM(Amount) as State_Revenue
FROM sales_data
GROUP BY State
ORDER BY State_Revenue DESC;

-- 6. Customer Segmentation by Gender and Age Group
SELECT 
    Gender,
    Age_Group,
    COUNT(DISTINCT User_ID) as Customer_Count,
    SUM(Amount) as Segment_Revenue
FROM sales_data
GROUP BY Gender, Age_Group
ORDER BY Segment_Revenue DESC;

-- 7. Festival vs Non-Festival Performance (Assuming Festival is Oct/Nov)
SELECT 
    CASE 
        WHEN Month IN ('Oct', 'Nov') THEN 'Festival Season'
        ELSE 'Regular Season'
    END as Season,
    SUM(Amount) as Revenue,
    COUNT(DISTINCT User_ID) as Active_Customers
FROM sales_data
GROUP BY Season;

-- 8. Occupation Analysis
SELECT 
    Occupation,
    SUM(Amount) as Revenue,
    AVG(Amount) as Avg_Spend_Per_Order
FROM sales_data
GROUP BY Occupation
ORDER BY Revenue DESC;
