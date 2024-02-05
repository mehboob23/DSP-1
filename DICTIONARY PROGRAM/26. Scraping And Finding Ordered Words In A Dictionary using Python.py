# Example Dictionary of Words
word_dict = {'apple': 1, 'banana': 2, 'cherry': 3, 'date': 4, 'grape': 5}

# Scraping And Finding Ordered Words In A Dictionary using Python
ordered_words = [word for word, _ in sorted(word_dict.items(), key=lambda x: x[1])]
print("Original Dictionary of Words:", word_dict)
print("Ordered Words:", ordered_words)
