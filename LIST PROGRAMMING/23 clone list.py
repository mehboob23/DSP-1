# Cloning or Copying a List
original_list = [int(x) for x in input("Enter space-separated elements of the original list: ").split()]
copied_list = original_list.copy()
print("Original List:", original_list)
print("Copied List:", copied_list)
