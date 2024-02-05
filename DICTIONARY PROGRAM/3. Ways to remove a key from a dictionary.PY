# Example Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Key to remove
key_to_remove = 'b'

# Remove a key from the Dictionary
if key_to_remove in my_dict:
    del my_dict[key_to_remove]
print("Original Dictionary:", "{'a': 1, 'b': 2, 'c': 3}")
print("Dictionary after removing key:", my_dict)
