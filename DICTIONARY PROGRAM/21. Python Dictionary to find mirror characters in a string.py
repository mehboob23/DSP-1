# Example String
my_string = "abcde"

# Python Dictionary to find mirror characters in a string
mirror_dict = {'a': 'e', 'b': 'd', 'c': 'c', 'd': 'b', 'e': 'a'}

mirror_characters = [mirror_dict[char] for char in my_string if char in mirror_dict]
print("Original String:", my_string)
print("Mirror Characters:", ''.join(mirror_characters))
