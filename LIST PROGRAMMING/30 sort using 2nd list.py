# Sort the Values of the First List Using the Second List
list1 = [int(x) for x in input("Enter space-separated elements of the first list: ").split()]
list2 = [int(x) for x in input("Enter space-separated elements of the second list: ").split()]
sorted_list1 = [x for _, x in sorted(zip(list1, list2))]
print("Sorted List1 based on values of List2:", sorted_list1)