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

def get_matrix_from_user(rows, cols):
    matrix = []
    print(f"Enter elements for a {rows}x{cols} matrix:")

    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)

    return matrix

# Get dimensions of matrices from user
rows = int(input("Enter the number of rows for the matrices: "))
cols = int(input("Enter the number of columns for the matrices: "))

# Get matrices from user
matrix_a = get_matrix_from_user(rows, cols)
matrix_b = get_matrix_from_user(rows, cols)

# Call the function to add matrices
result = add_matrices(matrix_a, matrix_b)

# Print the result
if result:
    print("\nMatrix A:")
    for row in matrix_a:
        print(row)

    print("\nMatrix B:")
    for row in matrix_b:
        print(row)

    print("\nSum of Matrices A and B:")
    for row in result:
        print(row)
