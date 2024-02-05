# Example Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Original Dictionary:", my_dict)
# Handling missing keys in Python dictionaries
key_to_lookup = input("Enter the key_to_lookup:")
default_value = 'Not Found'
value = my_dict.get(key_to_lookup, default_value)

print(f"Value for key '{key_to_lookup}':", value)
