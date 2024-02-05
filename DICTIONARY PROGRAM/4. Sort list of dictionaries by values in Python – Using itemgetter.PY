from operator import itemgetter

# Example List of Dictionaries
list_of_dicts = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]

# Sort list of dictionaries by values using itemgetter
sorted_list = sorted(list_of_dicts, key=itemgetter('age'))
print("Original List of Dictionaries:", list_of_dicts)
print("Sorted List of Dictionaries by 'age':", sorted_list)
