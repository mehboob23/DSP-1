from collections import defaultdict

# Example List of Words
word_list = ['listen', 'silent', 'enlist', 'trains', 'stars', 'arts']

# Print anagrams together in Python using List and Dictionary
anagrams_dict = defaultdict(list)
for word in word_list:
    sorted_word = ''.join(sorted(word))
    anagrams_dict[sorted_word].append(word)

print("Original List of Words:", word_list)
print("Anagrams together:", list(anagrams_dict.values()))
