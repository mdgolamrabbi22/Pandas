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
cpy_df["city"] = cpy_df["city"].fillna("Unknown_city")
cpy_df["city"] = cpy_df["city"].str.strip(
).str.title().str.replace("Nan", "Unknown_city")
cpy_df["delivery_days"] = cpy_df["delivery_days"].fillna(
    cpy_df["delivery_days"].median())

cpy_df["rating"] = cpy_df["rating"].fillna(cpy_df["rating"].median())
# print(cpy_df.isnull().sum())

# Duplicated Data Check
cpy_df = cpy_df.drop_duplicates()
# print(cpy_df.duplicated().sum())

cpy_df["order_date"] = pd.to_datetime(
    cpy_df["order_date"], format="mixed", dayfirst=True, errors="coerce")
cpy_df["price"] = (cpy_df["price"].astype("str")
                   .str.replace("TK", "", regex=False)
                   .str.replace(" ", "", regex=False)
                   .str.strip())
cpy_df["price"] = pd.to_numeric(
    cpy_df["price"],
    errors="coerce"
)
# print(cpy_df.dtypes)
# print(cpy_df["city"].unique())

print(cpy_df[(cpy_df["qty"] > 100) | (cpy_df["qty"] < 0)])
