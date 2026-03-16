import pandas as pd

# -----------------------------
# Test Case 1
# Load COVID dataset
# -----------------------------

covid = pd.read_csv("covid_data.csv")

print("COVID DATASET")

print("\nFirst 5 Records")
print(covid.head())

print("\nLast 5 Records")
print(covid.tail())

print("\nDataset Structure")
covid.info()

print("\nStatistical Summary")
print(covid.describe())

# Calculate recovery rate
covid["Recovery_Rate"] = (covid["Recovered"] / covid["Cases"]) * 100

print("\nDataset With Recovery Rate")
print(covid)


# -----------------------------
# Test Case 2
# Employee dataset analysis
# -----------------------------

employee = pd.read_csv("employee_data.csv")

print("\nEMPLOYEE DATASET")

print("\nFirst 5 Records")
print(employee.head())

print("\nDataset Structure")
employee.info()

print("\nStatistics for Age and Salary")
print(employee[["Age","Salary"]].describe())