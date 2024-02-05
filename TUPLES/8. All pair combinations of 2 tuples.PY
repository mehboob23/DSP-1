# Example Tuples
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')

# All pair combinations
result_combinations = [(x, y) for x in tuple1 for y in tuple2]
print("Original Tuples:", tuple1, tuple2)
print("All Pair Combinations:", result_combinations)
