# Example Tuple List
tuple_list = [(123, 'abc'), (456, 'def'), (789, 'ghi')]

# Extract digits from Tuple list
result_digits = [int(''.join(filter(str.isdigit, str(item)))) for item, _ in tuple_list]
print("Original Tuple List:", tuple_list)
print("Extracted Digits:", result_digits)
