def add_matrices(matrix1, matrix2):
    # Check if the matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrices must have the same dimensions for addition.")
        return None

    result_matrix = []

    # Iterate through each row
    for i in range(len(matrix1)):
        row = []

        # Iterate through each column in the row
        for j in range(len(matrix1[0])):
            # Add corresponding elements and append to the row
            row.append(matrix1[i][j] + matrix2[i][j])

        # Append the row to the result matrix
        result_matrix.append(row)

    return result_matrix

# Example matrices
matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Call the function to add matrices
result = add_matrices(matrix_a, matrix_b)

# Print the result
if result:
    print("Matrix A:")
    for row in matrix_a:
        print(row)

    print("\nMatrix B:")
    for row in matrix_b:
        print(row)

    print("\nSum of Matrices A and B:")
    for row in result:
        print(row)
