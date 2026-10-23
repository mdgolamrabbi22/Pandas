import pandas as pd

df = pd.read_csv("student_data_150.csv", index_col="Name")

# coloum Selection

# print(df["Name"].to_string())
# print(df["Id"].to_string())
# print(df["Age"].to_string())
# print(df[["Id", "Age", "Department"]])

# Row Selection

# print(df.loc["Fahim Ahmed", ["Id", "Age"]])
# print(df.iloc[0:15:2, 0:3])  # 0:15:2 Row and 0:3 coloum

# Task 1

Name = input("Enter Student Name :")

try:
    print(df.loc[Name])
except KeyError:
    print(f"{Name} is Not exist data list.")
