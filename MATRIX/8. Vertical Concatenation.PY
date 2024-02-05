matrix1 = [[1, 2],
           [3, 4]]
matrix2 = [[5, 6],
           [7, 8]]

vertical_concatenation = matrix1 + matrix2

print("Original Matrices:")
for row in matrix1 , matrix2:
  print(row)

print("\nVertical Concatenation:")
for row in vertical_concatenation:
    print(row)
