import numpy as np
print("MUHAMMED HISHAM KP , 41 , MCA-2022-24")

two_dimensional_complex_array = np.array([[1 + 2j, 2 + 3j, 3 + 4j],
                                         [4 + 5j, 5 + 6j, 6 + 7j]], dtype=complex)
print("2D Complex Array:")
print(two_dimensional_complex_array)
num_rows, num_cols = two_dimensional_complex_array.shape
array_dimension = two_dimensional_complex_array.ndim
reshaped_array = two_dimensional_complex_array.reshape(3, 2)

print("\na. Number of rows:", num_rows)
print("   Number of columns:", num_cols)
print("b. Dimension of the array:", array_dimension)
print("c. Reshaped array (3x2):")
print(reshaped_array)
