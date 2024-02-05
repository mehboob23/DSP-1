# Example Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2}

# Python – Keys associated with Values in Dictionary
associated_keys = [key for key, value in my_dict.items() if value == 2]
print("Original Dictionary:", my_dict)
print("Keys associated with value 2:", associated_keys)
