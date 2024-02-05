from collections import Counter

# Example List of Votes
votes = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice', 'Charlie', 'Charlie', 'Bob']

# Dictionary and Counter to find the winner of an election
vote_count = Counter(votes)
winner = max(vote_count, key=vote_count.get)
print("List of Votes:", votes)
print("Winner of the Election:", winner)
