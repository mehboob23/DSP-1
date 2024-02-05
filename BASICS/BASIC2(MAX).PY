# Function to find the maximum of two numbers
def find_maximum(num1, num2):
    return max(num1, num2)

number1 =float(input("Enter first number:"))
number2=float(input("Enter second number:"))

maximum_number = find_maximum(number1, number2)

print(f"Between your given numbers the maximum  is: {maximum_number}")
