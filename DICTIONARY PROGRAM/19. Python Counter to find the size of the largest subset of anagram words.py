from collections import Counter

# Example List of Words
word_list = ['listen', 'silent', 'enlist', 'trains', 'stars', 'arts']

# Python Counter to find the size of the largest subset of anagram words
anagram_counter = Counter(''.join(sorted(word)) for word in word_list)
largest_anagram_subset_size = max(anagram_counter.values(), default=0)

print("Original List of Words:", word_list)
print("Size of the largest subset of anagram words:", largest_anagram_subset_size)
