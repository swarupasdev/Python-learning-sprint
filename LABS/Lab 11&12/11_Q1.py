#q1-
# import numpy as np

# numbers = [1, 2.0, 3]
# # Convert list to numpy array
# numpy_array = np.array(numbers)
# # Convert elements to string type
# string_array = numpy_array.astype(str)

# print(string_array)

#q2 - 
import numpy as np

# # Create a 2D list
# list_2d = [[1, 2, 3], [4, 5, 6]]

# # Convert list to numpy array with dtype as int32
# numpy_array = np.array(list_2d, dtype='int32')

# print(numpy_array)

#q3 - 
# Create a 2D list
# list_2d = [[1, 2, 3], [4, 5, 6]]

# # Convert list to numpy array with dtype as int32
# numpy_array = np.array(list_2d, dtype='int32')

# # Get the number of rows and columns
# rows, cols = numpy_array.shape

# print(f'Number of rows: {rows}')
# print(f'Number of columns: {cols}')

# Q4 - 
import random

random_numbers = [random.randint(1, 100) for _ in range(10)]

print(random_numbers)
