# Example List
my_list = [1, 2, 3, 1, 2, 3, 4, 5]

# Counting the frequencies in a list using a dictionary in Python
frequency_dict = {}
for item in my_list:
    frequency_dict[item] = frequency_dict.get(item, 0) + 1

print("Original List:", my_list)
print("Frequency Dictionary:", frequency_dict)
