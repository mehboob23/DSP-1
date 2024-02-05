# Example Dictionary
my_dict = {'c': 1, 'a': 3, 'b': 2}

# Sort Python Dictionaries by Key
sorted_by_key = dict(sorted(my_dict.items()))
print("Original Dictionary:", my_dict)
print("Sorted Dictionary by Key:", sorted_by_key)

# Sort Python Dictionaries by Value
sorted_by_value = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Sorted Dictionary by Value:", sorted_by_value)
