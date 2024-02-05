# Find Cumulative Sum of a List
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
cumulative_sum = [sum(my_list[:i+1]) for i in range(len(my_list))]
print("Cumulative Sum List:", cumulative_sum)
