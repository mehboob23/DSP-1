# Example Nested Tuple
nested_tuple = ((1, 'a'), (2, 'b'), (3, 'c'))

# Convert Nested Tuple to Custom Key Dictionary
custom_key_dict = {key: value for key, value in nested_tuple}
print("Original Nested Tuple:", nested_tuple)
print("Converted Custom Key Dictionary:", custom_key_dict)
