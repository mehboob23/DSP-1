# Remove Empty Lists from a List
my_list = [eval(x) for x in input("Enter elements of the list (some may be empty lists): ").split()]
non_empty_lists = [sublist for sublist in my_list if sublist]
print("List after removing empty lists:", non_empty_lists)
