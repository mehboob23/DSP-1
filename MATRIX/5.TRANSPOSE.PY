matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transpose_matrix = list(map(list, zip(*matrix)))

print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix (Single Line):")
for row in transpose_matrix:
    print(row)
