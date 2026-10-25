import pandas as pd

df = pd.read_csv("Data.csv")


# Drop Coloumns
# print(df.drop(columns=["Email"]))

# Handle Missing data
# print(df.dropna(subset=["Age"]))
# print(df.fillna({"Age": "None"}))

# Fix Inconsint value

# df["Department"] = df["Department"].replace({"CST": "CSE",
#                                              "ET": "EEE",
#                                              "CMT": "CME"})
# print(df.to_string())


# Standard Text

# df["Name"] = df["Name"].str.upper()
# df["Name"] = df["Name"].str.lower()
# df["Name"] = df["Name"].str.startswith("A")
# df["Name"] = df["Name"].str.endswith("a")
# print(df.to_string())
# print(df.to_string())

# Change Data Type

# df["StudyHours"] = df["StudyHours"].astype(object)
# print(df.info())
# print(df.to_string())

# Remove Duplicates
# print(df[df.duplicated()])
# df = df.drop_duplicates()
# print(df[df.duplicated()])
