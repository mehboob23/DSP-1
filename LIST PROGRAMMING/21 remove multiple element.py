# Remove Multiple Elements from a List
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
elements_to_remove = [int(x) for x in input("Enter space-separated elements to remove: ").split()]
updated_list = [num for num in my_list if num not in elements_to_remove]
print("List after removing elements:", updated_list)
