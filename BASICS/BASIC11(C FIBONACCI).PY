import math

# Function to check if a number is a perfect square
def is_perfect_square(num):
    sqrt_num = int(math.sqrt(num))
    return sqrt_num * sqrt_num == num

def is_fibonacci_number(num):
    # A number is a Fibonacci number if and only if (5 * n^2 + 4) or (5 * n^2 - 4) is a perfect square
    condition1 = is_perfect_square(5 * num * num + 4)
    condition2 = is_perfect_square(5 * num * num - 4)
    
    return condition1 or condition2

number_to_check = int(input("Enter a number to check if it's a Fibonacci number: "))

if is_fibonacci_number(number_to_check):
    print(f"{number_to_check} is a Fibonacci number.")
else:
    print(f"{number_to_check} is not a Fibonacci number.")
