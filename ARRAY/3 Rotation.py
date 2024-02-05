# Function to left rotate an array by 'd' positions
def left_rotate_array(arr, d):
    n = len(arr)
    d = d % n      
    rotated_array = arr[d:] + arr[:d]
    return rotated_array


array = [int(x) for x in input("Enter space-separated elements of the array: ").split()]
rotation_distance = int(input("Enter the number of positions to left rotate: "))

rotated_array = left_rotate_array(array, rotation_distance)
print(f"The array after left rotation is: {rotated_array}")
