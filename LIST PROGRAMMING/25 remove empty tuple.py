# Remove Empty Tuples from a List
my_list = [eval(x) for x in input("Enter elements of the list (some may be empty tuples): ").split()]
non_empty_tuples = [tup for tup in my_list if tup]
print("List after removing empty tuples:", non_empty_tuples)
