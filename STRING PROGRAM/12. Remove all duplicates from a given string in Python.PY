string = "programming"
unique_characters = ''.join(sorted(set(string), key=string.index))
print("String after removing duplicates:", unique_characters)
