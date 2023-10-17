import numpy as np
print("MUHAMMED HISHAM KP , 41 , MCA-2022-24")

depth = int(input("Enter the depth of the array: "))
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

three_dimensional_array = np.random.rand(depth, rows, columns).astype(np.float32)

print("Generated 3D array:")
print(three_dimensional_array)