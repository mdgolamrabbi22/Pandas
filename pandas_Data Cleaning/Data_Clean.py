import pandas as pd

# Data Load
df = pd.read_csv("orders_messy.csv")

# Data Info Check
# print(df.head(10))
# print(df.info)
# print(df.dtypes)
# print(df.columns)
# print(df.shape)

# Data Cleaning

cpy_df = df.copy()
# print(cpy_df.head(10))

# Null Check
# print(cpy_df.isnull().sum())
# print(cpy_df.isnull().sum().sum())

# Column fixed
cpy_df.columns = cpy_df.columns.str.strip().str.lower().str.replace(" ", "_")
cpy_df.columns = cpy_df.columns.str.replace(
    "discount_%", "discount_percentage")
# print(cpy_df.columns)

# Null Data Fixed
cpy_df["payment_method"] = cpy_df["payment_method"].fillna("Unknown")
cpy_df["city"] = cpy_df["city"].fillna("Unknown_City")
cpy_df["city"] = cpy_df["city"].str.strip(
).str.title().str.replace("Nan", "Unknown_City")
cpy_df["delivery_days"] = cpy_df["delivery_days"].fillna(
    cpy_df["delivery_days"].median())

cpy_df["product"] = cpy_df["product"].str.strip().str.title()
cpy_df

cpy_df["rating"] = cpy_df["rating"].fillna(cpy_df["rating"].median())
# print(cpy_df.isnull().sum())

# Duplicated Data Check
cpy_df = cpy_df.drop_duplicates()
# print(cpy_df.duplicated().sum())

d1 = pd.to_datetime(cpy_df["order_date"], format="%Y-%m-%d", errors="coerce")
d2 = pd.to_datetime(cpy_df["order_date"], format="%d/%m/%Y", errors="coerce")
cpy_df["order_date"] = d1.fillna(d2)

cpy_df["price"] = pd.to_numeric(
    cpy_df["price"].astype(str).str.replace(r"[^\d.]", "", regex=True),
    errors="coerce")

# print(cpy_df.dtypes)
# print(cpy_df["city"].unique())

cpy_df["price"] = cpy_df["price"].mask(cpy_df["price"] > 100000)
cpy_df["qty"] = cpy_df["qty"].mask((cpy_df["qty"] < 1) | (cpy_df["qty"] > 10))
cpy_df["rating"] = cpy_df["rating"].mask(cpy_df["rating"] == 0)
cpy_df["delivery_days"] = cpy_df["delivery_days"].mask(
    cpy_df["delivery_days"] > 30)


cpy_df["price"] = cpy_df["price"].fillna(
    cpy_df.groupby("product")["price"].transform("median"))


for col in ["qty", "rating", "delivery_days"]:
    cpy_df[col] = cpy_df[col].fillna(cpy_df[col].median())

# print(cpy_df.isna().sum())
# print(cpy_df["city"].unique())
# print(cpy_df["product"].nunique())
# print(cpy_df["order_date"].min(), cpy_df["order_date"].max())
# print(cpy_df[["price", "qty", "rating", "delivery_days"]].describe())

cpy_df = cpy_df.to_csv("clean_data.csv", index=False)
