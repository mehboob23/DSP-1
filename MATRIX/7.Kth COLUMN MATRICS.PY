def get_kth_column(matrix, k):
    return [row[k] for row in matrix]

# Example matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = len(matrix)
cols = len(matrix[0])
print(matrix)
k = int(input("Enter the value of K (column index 0-2): ")) 
if 0 <= k < cols:
    # Call the function to get Kth column
    result_column = get_kth_column(matrix, k)

    print(f"{k}th Column of Matrix:")
    print(result_column)
else:
    print("Invalid K value. Please enter a valid column index.")
