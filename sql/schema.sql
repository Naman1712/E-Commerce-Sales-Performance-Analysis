-- SQL Schema for E-Commerce Sales Data
-- Database: PostgreSQL / MySQL Compatible

CREATE TABLE IF NOT EXISTS sales_data (
    User_ID VARCHAR(50),
    Cust_name VARCHAR(100),
    Product_ID VARCHAR(50),
    Gender VARCHAR(10),
    Age_Group VARCHAR(20),
    Age INT,
    Marital_Status INT,
    State VARCHAR(100),
    Zone VARCHAR(50),
    Occupation VARCHAR(100),
    Product_Category VARCHAR(100),
    Orders INT,
    Amount FLOAT,
    Order_Date DATE,
    Month VARCHAR(10),
    Year INT,
    Month_Num INT
);
