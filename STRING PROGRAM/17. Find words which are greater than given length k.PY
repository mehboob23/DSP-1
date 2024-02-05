string = "Python is great for programming"
k = 4
long_words = [word for word in string.split() if len(word) > k]
print(f"Words greater than {k} characters:", long_words)
