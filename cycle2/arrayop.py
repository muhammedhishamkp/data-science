import numpy as np

print("MUHAMMED HISHAM KP , 41 , MCA-2022-24")
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matrix2 = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])

# a. Add the two matrices and print the result
matrix_sum = matrix1 + matrix2
print("Matrix Addition:")
print(matrix_sum)

# b. Subtract the two matrices and print the result
matrix_diff = matrix1 - matrix2
print("\nMatrix Subtraction:")
print(matrix_diff)

# c. Multiply the individual elements of the matrices
elementwise_product = matrix1 * matrix2
print("\nElement-wise Multiplication:")
print(elementwise_product)

# d. Divide the elements of the matrices (assuming no division by zero)
elementwise_division = matrix1 / matrix2
print("\nElement-wise Division:")
print(elementwise_division)

# e. Perform matrix multiplication (dot product)
matrix_product = np.dot(matrix1, matrix2)
print("\nMatrix Multiplication:")
print(matrix_product)

# f. Display the transpose of a matrix
matrix1_transpose = np.transpose(matrix1)
print("\nTranspose of Matrix 1:")
print(matrix1_transpose)

# g. Calculate the sum of diagonal elements of a matrix
diagonal_sum = np.trace(matrix1)
print("\nSum of Diagonal Elements of Matrix 1:", diagonal_sum)

