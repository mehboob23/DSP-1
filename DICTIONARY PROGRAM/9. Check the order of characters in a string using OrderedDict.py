from collections import OrderedDict

# Example String
my_string = "Mehboob"

# Check order of characters in a string using OrderedDict
ordered_dict = OrderedDict.fromkeys(my_string)
is_ordered = my_string == ''.join(ordered_dict.keys())
print("Original String:", my_string)
print("Order of characters is maintained:", is_ordered)
