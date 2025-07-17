def rotate_matrix(matrix):
    """
    Rotates the given square matrix 90 degrees clockwise in place.

    Args:
        matrix: the 2D square matrix to rotate
    """
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp
    return matrix


def print_matrix(matrix):
    """
    Helper function to print a 2D matrix.

    Args:
        matrix: the matrix to print
    """
    for row in matrix:
        print(' '.join(str(value) for value in row))


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Original Matrix:")
    print_matrix(matrix)
    rotate_matrix(matrix)
    print("Matrix after 90-degree clockwise rotation:")
    print_matrix(matrix)

    # Expected output:
    # Original Matrix:
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # Matrix after 90-degree clockwise rotation:
    # 7 4 1
    # 8 5 2
    # 9 6 3