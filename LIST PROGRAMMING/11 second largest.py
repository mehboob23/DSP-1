# Find Second Largest Number in a List
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
sorted_list = sorted(my_list, reverse=True)
second_largest_number = sorted_list[1]
print("Second Largest Number:", second_largest_number)
