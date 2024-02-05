def contains_all_vowels(s):
    vowels = set('aeiou')
    return set(s.lower()) >= vowels

string = "AEIOU are vowels"
if contains_all_vowels(string):
    print(f"{string} contains all vowels.")
else:
    print(f"{string} does not contain all vowels.")
