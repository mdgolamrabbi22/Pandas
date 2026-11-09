import pandas as pd

data = [10, 20, 50, 40]

# series convert / label(index) convert
series = pd.Series(data, index=["a", "b", "c", "d"])
# print(series)

# data accesing and data replace
# series.loc["a"] = 50

# iloc diya int index select kore data access naoya hoi
# print(series.iloc[0])

# loc diya int and custom_index select kore data access naoya hoi
# print(series.loc["a"])


# data fieltaring simple
# print(series[series <= 20])

calories = {"Day 1": 1500,
            "Day 2": 1800,
            "Day 3": 2500,
            "Day 4": 2800,
            "Day 5": 3500}

se_cal = pd.Series(calories)
print(se_cal[(se_cal >= 2000) & (se_cal <= 3000)])
