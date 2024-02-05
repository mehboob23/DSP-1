# Print Positive Numbers in a List
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
positive_numbers = [num for num in my_list if num > 0]
print("Positive Numbers:", positive_numbers)
