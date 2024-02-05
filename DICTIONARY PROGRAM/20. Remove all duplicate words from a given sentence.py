# Example Sentence
my_sentence = "this is a test sentence is a test"

# Remove all duplicate words from a given sentence
unique_words = ' '.join(dict.fromkeys(my_sentence.split()))
print("Original Sentence:", my_sentence)
print("Sentence after removing duplicate words:", unique_words)
