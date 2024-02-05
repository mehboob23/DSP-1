from collections import OrderedDict

# Example OrderedDict
ordered_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Key-Value to insert at the beginning
new_key, new_value = 'x', 0

# Insertion at the beginning in OrderedDict
ordered_dict = OrderedDict([(new_key, new_value)] + list(ordered_dict.items()))
print("original orderedDict:","([('a', 1), ('b', 2), ('c', 3)])")
print("AFTER insertion new_value ('x', 0) OrderedDict:", ordered_dict)
