# Example List of Tuples
list_of_tuples = [(3, 'b'), (1, 'a'), (2, 'c')]

# Sort by the second item
sorted_tuples = sorted(list_of_tuples, key=lambda x: x[1])
print("Original List of Tuples:", list_of_tuples)
print("Sorted List of Tuples:", sorted_tuples)
