import numpy as np

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_tuple = ([8, 4, 6], [1, 2, 3])

list_to_array = np.array(my_list)
tuple_to_array = np.array(my_tuple)

print("List to array:")
print(list_to_array)

print("\nTuple to array:")
print(tuple_to_array)
