# Function to calculate the sum of an array
def sum_of_array(arr):
    return sum(arr)


array = [int(x) for x in input("Enter space-separated elements of the array: ").split()]

result = sum_of_array(array)
print(f"The sum of the array is: {result}")
