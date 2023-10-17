import numpy as np

print("MUHAMMED HISHAM KP , 41 , MCA-2022-24")
arr_1d = np.array(list(map(int, input("Enter elements for 1D array separated by spaces: ").split())))

# Using diag() (should be empty for 1D array)
diag_1d = np.diag(arr_1d)

print("\nOriginal 1D Array:")
print(arr_1d)

print("\nDiagonal Elements (empty for 1D array):")
print(diag_1d)


# User input for a square 2D array
n = int(input("Enter the size of the square matrix: "))
square_matrix = np.array([list(map(int, input().split())) for _ in range(n)])

# Using diag() to extract diagonal elements of the square matrix
diag_square_matrix = np.diag(square_matrix)

print("\nOriginal Square Matrix:")
print(square_matrix)

print("\nDiagonal Elements of Square Matrix:")
print(diag_square_matrix)