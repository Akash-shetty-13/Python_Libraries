# Import numpy library for matrix operations
import numpy as np

# Step 1: Create traffic flow matrix (2x2)
# Rows represent source roads
# Columns represent destination roads
# Example:
# 200 vehicles go from Road 1 to Road 1
# 150 vehicles go from Road 1 to Road 2
# 100 vehicles go from Road 2 to Road 1
# 250 vehicles go from Road 2 to Road 2
A = np.array([
    [200, 150],
    [100, 250]
])

# Step 2: Create transformation matrix
# This represents signal timing change
# 0.8 means 80% traffic continues in same direction
# 0.2 means 20% traffic shifts
# 0.3 and 0.7 represent redistribution for Road 2
T = np.array([
    [0.8, 0.2],
    [0.3, 0.7]
])

# Step 3: Multiply matrices
# This simulates new traffic after signal optimization
A_new = np.dot(A, T)

# Step 4: Print original and new traffic data
print("Original Traffic Matrix:")
print(A)

print("\nTransformation Matrix:")
print(T)

print("\nNew Traffic Matrix After Signal Optimization:")
print(A_new)

# Step 5: Compare total traffic before and after
# Total traffic should remain same if redistribution only
print("\nTotal traffic before optimization:", np.sum(A))
print("Total traffic after optimization:", np.sum(A_new))