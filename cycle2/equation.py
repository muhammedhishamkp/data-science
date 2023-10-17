import numpy as np

print("MUHAMMED HISHAM KP , 41 , MCA-2022-24")
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

X = np.empty((rows, cols), dtype=float)
print("Enter first matrix")
for i in range(rows):
    for j in range(cols):
        X[i, j] = float(input(f"Enter the value for X[{i}][{j}]: "))

Y = np.empty((rows, cols), dtype=float)

print("Enter second matrix")
for i in range(rows):
    for j in range(cols):
        Y[i, j] = float(input(f"Enter the value for Y[{i}][{j}]: "))

result = X**2 + 2*Y

print("Matrix X:")
print(X)
print("Matrix Y:")
print(Y)
print("Result (X^2 + 2Y):")
print(result)
