from katas.matrix_rotate import rotate_matrix
import unittest 
class TestMatrixRotate(unittest.TestCase):
    def test_rotate_matrix_90_degrees(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected_output = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        result = rotate_matrix(matrix)
        self.assertEqual(result, expected_output)

    def test_rotate_empty_matrix(self):
        matrix = []
        expected_output = []
        result = rotate_matrix(matrix)
        self.assertEqual(result, expected_output)

    def test_rotate_single_element_matrix(self):
        matrix = [[42]]
        expected_output = [[42]]
        result = rotate_matrix(matrix)
        self.assertEqual(result, expected_output)