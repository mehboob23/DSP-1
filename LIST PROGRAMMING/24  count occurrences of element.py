# Count Occurrences of an Element in a List
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
element_to_count = int(input("Enter the element to count: "))
occurrences = my_list.count(element_to_count)
print(f"Number of occurrences of {element_to_count}: {occurrences}")
