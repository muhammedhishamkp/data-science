import numpy as np

print("MUHAMMED HISHAM KP , 41 , MCA-2022-24")
arr_1d = np.array([1, 2, 3, 4, 5])

# User input for value and index
value_to_insert = int(input("Enter the value to insert: "))
index_to_insert = int(input(f"Enter the index to insert {value_to_insert} at: "))

# Using insert() to insert the value at the specified index
new_arr_1d = np.insert(arr_1d, index_to_insert, value_to_insert)

print("Original 1D Array:")
print(arr_1d)

print(f"\nArray after inserting {value_to_insert} at index {index_to_insert}:")
print(new_arr_1d)

# Creating a 2D array
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# User input for values and index
values_to_insert = list(map(int, input("Enter values to insert in the format 'x y z': ").split()))
index_to_insert = int(input(f"Enter the index to insert {values_to_insert} at: "))

# Using insert() to insert the values at the specified index along axis 0
new_arr_2d = np.insert(arr_2d, index_to_insert, values_to_insert, axis=0)

print("\nOriginal 2D Array:")
print(arr_2d)

print(f"\nArray after inserting {values_to_insert} at index {index_to_insert} along axis 0:")
print(new_arr_2d)
