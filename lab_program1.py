import numpy as np

# -----------------------------
# Basic Array Operations using NumPy
# -----------------------------

print("=== Test Case 1: 3x3 Array Creation and Reshaping ===")

# Create 3x3 array (3 subjects × 3 students)
marks = np.array([
    [70, 80, 75],
    [85, 78, 90],
    [60, 88, 72]
])

print("Original 3x3 Matrix:\n", marks)

# Reshape to (1, 9)
reshaped = marks.reshape(1, 9)
print("\nReshaped to (1,9):\n", reshaped)


print("\n=== Test Case 2: Element-wise Multiplication ===")

arr1 = np.array([2, 4, 6])
arr2 = np.array([3, 5, 7])

result = arr1 * arr2
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Element-wise Multiplication:", result)


print("\n=== Application Task: Teacher Assessment Processing ===")

# Double marks of Subject 2 for bonus
marks[:, 1] *= 2

print("After Bonus (Subject 2 Doubled):\n", marks)

# Convert to single row format
report_format = marks.flatten()
print("\nSingle Row Report Format:\n", report_format)

# Calculate total marks per student
total_marks = marks.sum(axis=0)
print("\nTotal Marks per Student:\n", total_marks)