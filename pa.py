import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Hina", "Bilal"],
    "Department": ["IT", "HR", "Finance", "IT", "Finance", "HR"],
    "Salary": [70000, 50000, 65000, 80000, 60000, 55000],
    "Experience": [2, 5, 3, 7, 1, 4]
}

df = pd.DataFrame(data)

# Department wise salary analysis
print(df.groupby("Department")["Salary"].agg(["mean", "max", "min"]))

# Experience bucket
df["Exp_Level"] = pd.cut(df["Experience"], bins=[0,2,5,100], labels=["Junior","Mid","Senior"])
print(df)
