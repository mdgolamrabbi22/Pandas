import pandas as pd

student_data = {
    "Name": ["GR", "MT", "RK", "MS"],
    "Age": [20, 21, 22, 23],
    "Roll": [10, 15, 18, 74]
}

df = pd.DataFrame(student_data, index=[
                  "Student 1", "Student 2", "Student 3", "Student 4"])

# adding new coloum
df["Profetion"] = ["DT", "ML", "APP", "CS"]

# adding new rows
new_Rows = pd.DataFrame([{"Name": "SD", "Age": 20, "Roll": 25, "Profetion": "DM"},
                         {"Name": "HR", "Age": 22, "Roll": 24, "Profetion": "NW"},
                         {"Name": "MN", "Age": 23, "Roll": 20, "Profetion": "AI"}],
                        index=["Student 5", "Student 6", "Student 7"])

df = pd.concat([df, new_Rows])

print(df)
