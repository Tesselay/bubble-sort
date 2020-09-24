import unittest
import bubbleSort


class TestSorting(unittest.TestCase):
    def test_simple_list(self):
        numbers = [1, 5, 3, 2, 9, 4, 7, 8, 0, 6]
        numbers = bubbleSort.bubble_sort(numbers)

        sorted_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(numbers, sorted_numbers, "Should be of same order")

    def test_negative_list(self):
        numbers = [-3, 2, -1, -7, 4, 9, -12, -11, 5, 7]
        numbers = bubbleSort.bubble_sort(numbers)

        sorted_numbers = [-12, -11, -7, -3, -1, 2, 4, 5, 7, 9]
        self.assertEqual(numbers, sorted_numbers, "Should be of same order")


if __name__ == '__main__':
    unittest.main()
