import string

def contains_special_characters(s):
    special_characters = set(string.punctuation)
    return any(char in special_characters for char in s)

input_string = "Hello @World!"
if contains_special_characters(input_string):
    print(f"{input_string} contains special characters.")
else:
    print(f"{input_string} does not contain special characters.")
