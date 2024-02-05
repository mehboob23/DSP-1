# Example Characters
given_characters = 'apple'

# Example List of Words
word_list = ['ap', 'pale', 'peal', 'apple', 'plae']

# Possible Words using given characters in Python
possible_words = [word for word in word_list if all(word.count(char) <= given_characters.count(char) for char in word)]
print("Given Characters:", given_characters)
print("Original List of Words:", word_list)
print("Possible Words:", possible_words)
