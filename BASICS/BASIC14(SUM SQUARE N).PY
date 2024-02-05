# Function to calculate the sum of squares of first n natural numbers
def sum_of_squares(n):
    return (n * (n + 1) * (2 * n + 1)) // 6

n = int(input("Enter the value of n: "))

if n < 0:
    print("Please enter a non-negative integer.")
else:
    result = sum_of_squares(n)
    print(f"The sum of squares of the first {n} natural numbers is: {result}")
