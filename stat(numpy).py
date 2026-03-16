import numpy as np

# -----------------------------
# Test Case 1
# Standard deviation of weekly rainfall
# -----------------------------

rainfall = np.array([12, 18, 25, 10, 30, 22, 16])

print("Weekly Rainfall Data (mm):")
print(rainfall)

rainfall_std = np.std(rainfall)

print("Standard Deviation of Rainfall:", rainfall_std)


# -----------------------------
# Test Case 2
# Mean and median of student scores
# -----------------------------

scores = np.array([72, 85, 90, 68, 75, 88, 95, 70])

print("\nStudent Exam Scores:")
print(scores)

mean_score = np.mean(scores)
median_score = np.median(scores)

print("Mean Score:", mean_score)
print("Median Score:", median_score)


# -----------------------------
# Scenario
# Climate stability analysis
# -----------------------------

temperature = np.array([30, 32, 31, 29, 35, 33, 34, 36, 31, 30])

print("\nDaily Temperature Data (°C):")
print(temperature)

mean_temp = np.mean(temperature)
median_temp = np.median(temperature)
variance_temp = np.var(temperature)
std_temp = np.std(temperature)

print("\nTemperature Statistics")
print("Mean Temperature:", mean_temp)
print("Median Temperature:", median_temp)
print("Variance:", variance_temp)
print("Standard Deviation:", std_temp)


# -----------------------------
# Climate Stability Evaluation
# -----------------------------

if std_temp < 2:
    print("\nClimate is stable. Temperature variation is low.")
elif std_temp < 5:
    print("\nModerate temperature variation detected.")
else:
    print("\nHigh variation detected. Possible irregular climate behavior.")