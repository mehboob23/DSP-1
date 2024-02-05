# Function to check if a number is an Armstrong number
def is_armstrong_number(number):
    # Calculate the number of digits in the given number
    num_digits = len(str(number))
    
    # Calculate the sum of each digit raised to the power of the number of digits
    total = sum(int(digit) ** num_digits for digit in str(number))
    
    # Check if the total is equal to the original number
    return total == number

num = int(input("Enter a  number: "))

if is_armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
