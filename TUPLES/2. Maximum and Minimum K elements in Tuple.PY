# Example Tuple
my_tuple = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)

# K value
k = 3

# Maximum K elements
max_k_elements = tuple(sorted(my_tuple)[-k:])
print("Tuple:", my_tuple)
print(f"Maximum {k} elements in the Tuple:", max_k_elements)

# Minimum K elements
min_k_elements = tuple(sorted(my_tuple)[:k])
print(f"Minimum {k} elements in the Tuple:", min_k_elements)
