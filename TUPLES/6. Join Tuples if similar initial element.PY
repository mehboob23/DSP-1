# Example Tuples
tuples_list = [(1, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (3, 'e')]

# Join Tuples with similar initial element
result_dict = {}
for key, value in tuples_list:
    result_dict.setdefault(key, []).append(value)

result_list = [(key, ' '.join(values)) for key, values in result_dict.items()]
print("Original Tuples:", tuples_list)
print("Joined Tuples:", result_list)
