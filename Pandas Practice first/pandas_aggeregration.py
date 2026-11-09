import pandas as pd

df = pd.read_csv("student_data_150.csv")

# Whole Data Frame

# print(df.mean(numeric_only=True))
# print(df.median(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.count())

# Single Column

# print(df["Age"].mean())
# print(df["Age"].sum())
# print(df["Age"].median())
# print(df["Age"].max())
# print(df["Age"].min())
# print(df["Age"].count())

# Group by

group = df.groupby("Department")

# print(group["Age"].mean())
# print(group["Age"].median())
# print(group["Age"].sum())
# print(group["Age"].max())
# print(group["Age"].min())
# print(group["Age"].count())

# Data Replace

df["Department"] = df["Department"].replace({"CST": "CSE"})
print(df.to_string())
