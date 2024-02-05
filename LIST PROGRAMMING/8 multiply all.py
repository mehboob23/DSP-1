# Multiply All Numbers in a List
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
product = 1
for num in my_list:
    product *= num
print("Product of Numbers:", product)
