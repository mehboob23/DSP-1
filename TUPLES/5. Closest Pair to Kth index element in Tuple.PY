# Example Tuple
my_tuple = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)

# K value
k = 3

# Closest Pair to Kth index element
closest_pair = min(my_tuple, key=lambda x: abs(x - my_tuple[k]))
print("Tuple:", my_tuple)
print(f"Closest Pair to {k}th index element:", closest_pair)
