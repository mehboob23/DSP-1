# Existing List
my_list = [1, 2, 3]

# Tuple to add to the list
new_tuple = (4, 5, 6)

# Adding Tuple to List
list_with_tuple = my_list + list(new_tuple)
print("Original List:", my_list)
print("Tuple to Add:", new_tuple)
print("List with Tuple:", list_with_tuple)

# Converting List to Tuple
tuple_from_list = tuple(my_list) + new_tuple
print("List to Convert:", my_list)
print("Tuple from List:", tuple_from_list)
