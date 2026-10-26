import pandas as pd
import matplotlib.pyplot as plt


# Step-1 : CSV File Load kora

df = pd.read_csv("messy_ecommerce_orders_1500.csv")

# print(df.head())
# print(df.shape)
# print(df.columns)
# print(df.info())
# print(df.describe())

# Step-2 : Data Quality check

# Missing Value check
# print(df.isnull().sum())

# Total missing value Check
# print(df.isnull().sum().sum())

# Missing value Percentage
missing_value = (df.isnull().sum() / len(df)) * 100
# print(missing_value)

# Duplicate Row
# print(df.duplicated().sum())

# Data Type Check
# print(df.dtypes)

# Unique Row Data Check
# print(df["Order_Status"].unique())
# print(df["Payment_Method"].unique())
# print(df["City"].unique())

# Step-3 : Data Cleaning kora

clean_df = df.copy()
# print(clean_df.isnull().sum())

# Clean Age Column
age_median = clean_df["Age"].median()
clean_df["Age"] = clean_df["Age"].fillna(age_median)

# FIll Customer_Name Column
clean_df["Customer_Name"] = clean_df["Customer_Name"].fillna("Unknown")

# Remove Duplicated row
# print(clean_df.duplicated().sum())
clean_df = clean_df.drop_duplicates()
# print(clean_df.duplicated().sum())

# Check Order_ID duplicate
# print(clean_df["Order_ID"].duplicated().sum())

# Check City, Payment_Method, Order_Status, Sales_Channel

clean_df["City"] = clean_df["City"].str.strip().str.title()
clean_df["Payment_Method"] = clean_df["Payment_Method"].str.strip().str.title()
clean_df["Order_Status"] = clean_df["Order_Status"].str.strip().str.title()
clean_df["Sales_Channel"] = clean_df["Sales_Channel"].str.strip().str.title()

clean_df["Product_Category"] = clean_df["Product_Category"].str.strip().str.title()
clean_df["Product_Category"] = clean_df["Product_Category"].replace({
    "Electronic": "Electronics",
    "Cloth": "Clothing"
})

# print(clean_df["Product_Category"].unique())

clean_df["Order_Date"] = pd.to_datetime(
    clean_df["Order_Date"],
    format="mixed",
    dayfirst=True,
    errors="coerce"
)
# print(clean_df["Order_Date"].isnull().sum())


# Invalid numeric values Test
# print(clean_df[clean_df["Age"] < 0])
# print(clean_df[clean_df["Age"] > 100])

# print(clean_df[clean_df["Quantity"] <= 0])
# print(clean_df[clean_df["Unit_Price_BDT"] <= 0])
# print(clean_df[clean_df["Discount_Percent"] > 100])
# print(clean_df[clean_df["Discount_Percent"] < 0])

# print(clean_df[
#     (clean_df["Customer_Rating"] < 1) |
#     (clean_df["Customer_Rating"] > 5)
# ])

# print(clean_df[clean_df["Delivery_Days"] <= 0])

# clean_df.to_csv("cleaned_ecommerce_orders.csv", index=False)

# Step-4 : Feature Engineering

clean_df["Gross_Sales_BDT"] = (
    clean_df["Quantity"] * clean_df["Unit_Price_BDT"]
)

# print(clean_df[[
#     "Quantity",
#     "Unit_Price_BDT",
#     "Gross_Sales_BDT"
# ]].head())


clean_df["Discount_Amount_BDT"] = (
    clean_df["Gross_Sales_BDT"] * clean_df["Discount_Percent"] / 100
)

# print(clean_df[[
#     "Discount_Amount_BDT",
#     "Gross_Sales_BDT",
#     "Discount_Percent"
# ]].head())

clean_df["Net_Sales_BDT"] = (
    clean_df["Gross_Sales_BDT"] - clean_df["Discount_Amount_BDT"]
)

# print(clean_df[[
#     "Net_Sales_BDT",
#     "Gross_Sales_BDT",
#     "Discount_Amount_BDT"
# ]].head())

clean_df["Year"] = clean_df["Order_Date"].dt.year
clean_df["Month"] = clean_df["Order_Date"].dt.month

# print(clean_df[[
#     "Order_Date",
#     "Year",
#     "Month"
# ]].head())


# print(clean_df[[
#     "Order_ID",
#     "Quantity",
#     "Unit_Price_BDT",
#     "Gross_Sales_BDT",
#     "Discount_Amount_BDT",
#     "Net_Sales_BDT",
#     "Year",
#     "Month"
# ]].head(10))

# Step-5 : Sales Data Analysis

# print("Total orders:", len(clean_df))
# print("Total quantity sold:", clean_df["Quantity"].sum())

total_sales = clean_df["Net_Sales_BDT"].sum()
# print("Total Net Sales:", total_sales, "BDT")

average_order_value = clean_df["Net_Sales_BDT"].mean()
# print("Average_order_value", average_order_value, "BDT")

category_sales = clean_df.groupby("Product_Category")["Net_Sales_BDT"].sum()
# print(category_sales.sort_values(ascending=False))

top_product = (
    clean_df.groupby("Product_Category")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
# print(top_product)

top_city = (
    clean_df.groupby("City")["Net_Sales_BDT"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
# print(top_city)

status_count = clean_df["Order_Status"].value_counts()
# print(status_count)

status_percent = clean_df["Order_Status"].value_counts(normalize=True) * 100
# print(status_percent)

payment_methoud = clean_df["Payment_Method"].value_counts()
# print(payment_methoud)

monthly_sales = (
    clean_df.groupby(["Year", "Month"])["Net_Sales_BDT"]
    .sum()
    .head(10)
)

# print(monthly_sales)


# Step-6 : Data Visualization

# Show chart catagory sales

plt.close("all")

category_sales = (
    clean_df.groupby("Product_Category")["Net_Sales_BDT"]
    .sum()
    .sort_values(ascending=True)
)

plt.figure(figsize=(9, 6))

category_sales.plot(kind="barh")

plt.title("Net Sales by Product Category")
plt.xlabel("Net Sales (BDT)")
plt.ylabel("Product Category")
plt.tight_layout()
# plt.show()


# Monthly Sales Trend

plt.close("all")

monthly_sales = (
    clean_df.groupby(["Year", "Month"])["Net_Sales_BDT"]
    .sum()
)

monthly_sales.index = [
    f"{year}-{month:02}"
    for year, month in monthly_sales.index
]

plt.figure(figsize=(10, 5))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Year-Month")
plt.ylabel("Net Sales (BDT)")
plt.xticks(rotation=45)
plt.tight_layout()
# plt.show()

# Top 10 Products

plt.close("all")

top_products = (
    clean_df.groupby("Product_Name")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))
top_products.sort_values().plot(kind="barh")

plt.title("Top 10 Products by Quantity Sold")
plt.xlabel("Total Quantity Sold")
plt.ylabel("Product Name")
plt.tight_layout()
# plt.show()

# Order Status Distribution

plt.close("all")
plt.figure(figsize=(7, 7))

status_count = clean_df["Order_Status"].value_counts()

status_count.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Order Status Distribution")
plt.ylabel("")
plt.tight_layout()
# plt.show()


plt.close("all")

plt.figure(figsize=(8, 5))

clean_df["Age"].dropna().plot(
    kind="hist",
    bins=15,
    edgecolor="black"
)

plt.title("Customer Age Distribution")
plt.xlabel("Customer Age")
plt.ylabel("Number of Records")
plt.tight_layout()
# plt.show()


# part-7: Bussines insights

# # 1. Total sales
# total_sales = clean_df["Net_Sales_BDT"].sum()
# print("Total Net Sales:", round(total_sales, 2), "BDT")

# # 2. Average sales per row
# average_sales = clean_df["Net_Sales_BDT"].mean()
# print("Average Sales:", round(average_sales, 2), "BDT")

# # 3. Best-selling category
# category_sales = clean_df.groupby(
#     "Product_Category"
# )["Net_Sales_BDT"].sum()

# best_category = category_sales.idxmax()
# print("Best-Selling Category:", best_category)

# # 4. Lowest-selling category
# lowest_category = category_sales.idxmin()
# print("Lowest-Selling Category:", lowest_category)

# # 5. Most popular payment method
# payment_method = clean_df["Payment_Method"].mode()

# if not payment_method.empty:
#     print("Most Popular Payment Method:", payment_method.iloc[0])

# # 6. Order status summary
# print("\nOrder Status Summary:")
# print(clean_df["Order_Status"].value_counts())
