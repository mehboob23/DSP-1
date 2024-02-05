# Print Duplicates from a List of Integers
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
duplicates = set([num for num in my_list if my_list.count(num) > 1])
print("Duplicates in the List:", list(duplicates))
