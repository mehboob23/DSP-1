# Example Tuple of Lists
tuple_of_lists = ([1, 2, 3], ['a', 'b', 'c'], [4, 5, 6])

# Flatten Tuple of Lists to Tuple
flattened_tuple = tuple(item for sublist in tuple_of_lists for item in sublist)
print("Original Tuple of Lists:", tuple_of_lists)
print("Flattened Tuple:", flattened_tuple)
