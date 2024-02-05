def add_matrices(matrix1, matrix2):
    result_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result_matrix

def subtract_matrices(matrix1, matrix2):
    result_matrix = [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result_matrix

# Example matrices
matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result_addition = add_matrices(matrix_a, matrix_b)
result_subtraction = subtract_matrices(matrix_a, matrix_b)

print("Matrix Addition:")
for row in result_addition:
    print(row)

print("\nMatrix Subtraction:")
for row in result_subtraction:
    print(row)
