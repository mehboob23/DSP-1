def multiply_matrices(matrix1, matrix2):
    # Check if the number of columns in the first matrix is equal to the number of rows in the second matrix
    if len(matrix1[0]) != len(matrix2):
        print("Matrix multiplication is not possible. Number of columns in Matrix 1 must be equal to the number of rows in Matrix 2.")
        return None

    result_matrix = []

    # Iterate through each row in the first matrix
    for i in range(len(matrix1)):
        row = []

        # Iterate through each column in the second matrix
        for j in range(len(matrix2[0])):
            # Calculate the dot product of the corresponding row in the first matrix and column in the second matrix
            dot_product = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2)))

            # Append the dot product to the row
            row.append(dot_product)

        # Append the row to the result matrix
        result_matrix.append(row)

    return result_matrix

# Predefined matrices
matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_b = [
    [9],
    [6],
    [3]
]

# Call the function to multiply matrices
result = multiply_matrices(matrix_a, matrix_b)

# Print the result
if result:
    print("\nMatrix A:")
    for row in matrix_a:
        print(row)

    print("\nMatrix B:")
    for row in matrix_b:
        print(row)

    print("\nProduct of Matrices A and B:")
    for row in result:
        print(row)
