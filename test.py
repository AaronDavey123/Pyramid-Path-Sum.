import unittest
from max_path import maximum_path

class TestMaximumPath(unittest.TestCase):

    # Test Case 1: Simple pyramid with a clear path
    def test_simple_pyramid(self):
        node_values = [
            3,
            4, 6,
            5, 7, 8,
            9, 1, 2, 3
        ]
        expected_result = 21  # Corrected expected result (3 -> 6 -> 7 -> 5 = 21)
        actual_result = maximum_path(node_values)
        self.assertEqual(actual_result, expected_result)
    
    # Test Case 2: A pyramid with only one row (edge case)
    def test_single_row(self):
        node_values = [5]
        expected_result = 5  # Only one value, so it's the path sum.
        actual_result = maximum_path(node_values)
        self.assertEqual(actual_result, expected_result)
    
    # Test Case 3: A pyramid with multiple rows and a different set of values
    def test_large_pyramid(self):
        node_values = [
            10,
            2, 5,
            3, 6, 1,
            8, 9, 4, 7
        ]
        expected_result = 30  # Corrected expected result (10 -> 5 -> 6 -> 9 = 30)
        actual_result = maximum_path(node_values)
        self.assertEqual(actual_result, expected_result)

if __name__ == "__main__":
    unittest.main()
