# Example List of Tuples
list_of_tuples = [(3, 'b'), (1, 'a'), (2, 'c')]

# External List for Ordering
order_list = [2, 1, 3]

# Order Tuples using External List
ordered_tuples = [tup for _, tup in sorted(zip(order_list, list_of_tuples))]
print("Original List of Tuples:", list_of_tuples)
print("Ordered Tuples using External List:", ordered_tuples)
