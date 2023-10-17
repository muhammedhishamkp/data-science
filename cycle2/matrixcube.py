import numpy as np

print("MUHAMMED HISHAM KP , 41 , MCA-2022-24")
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

X = np.empty((rows, cols), dtype=int)
for i in range(rows):
    for j in range(cols):
        X[i, j] = int(input(f"Enter the element at row {i+1}, column {j+1}: "))

cubed_matrix_multiply = X * X * X

cubed_matrix_power = np.power(X, 3)
cubed_matrix_double_asterisk = X ** 3

# Display the results
print("\nCube of each element using multiplication:\n", cubed_matrix_multiply)
print("\nCube of each element using power function:\n", cubed_matrix_power)
print("\nCube of each element using double asterisk (**):\n", cubed_matrix_double_asterisk)

if rows == cols:
    identity_matrix = np.identity(rows)
    print("\nIdentity matrix of X:\n", identity_matrix)
else:
    print("\nX is not a square matrix, so it doesn't have an identity matrix.")

powers = [2, 3, 4]
powered_matrices = [np.power(X, p) for p in powers]

for i, p in enumerate(powers):
    print(f"\nMatrix raised to the power {p}:\n", powered_matrices[i])