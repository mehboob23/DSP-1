# Method 1: Using the clear() method
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
my_list1 = my_list.copy()
my_list1.clear()
print("Method 1 - List after clear:", my_list1)

# Method 2: Assigning an empty list
my_list2 = my_list.copy()
my_list2 = []
print("Method 2 - List after assigning an empty list:", my_list2)

# Method 3: Using list slicing
my_list3 = my_list.copy()
my_list3[:] = []
print("Method 3 - List after using list slicing:", my_list3)

# Method 4: Using the *= 0 operator
my_list4 = my_list.copy()
my_list4 *= 0
print("Method 4 - List after using *= 0:", my_list4)

# Method 5: Using pop() in a loop
my_list5 = my_list.copy()
while my_list5:
    my_list5.pop()
print("Method 5 - List after using pop in a loop:", my_list5)
