# Function to print ASCII value of a character
def print_ascii_value(char):
    ascii_value = ord(char)
    print(f"The ASCII value of '{char}' is: {ascii_value}")

character = input("Enter a character: ")

if len(character) == 1:
    print_ascii_value(character)
else:
    print("Please enter a single character.")
