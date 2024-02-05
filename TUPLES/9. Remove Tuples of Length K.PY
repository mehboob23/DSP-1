# Example Tuple List
tuple_list = [(1, 2), (3, 4, 5), (6, 7, 8), (9, 10)]

# K value
k = 2

# Remove Tuples of Length K
filtered_tuples = [tup for tup in tuple_list if len(tup) != k]
print("Original Tuple List:", tuple_list)
print("Tuples after removing length", k, ":", filtered_tuples)
