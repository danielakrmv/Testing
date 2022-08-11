import my_math
import unittest


class TestAdd(unittest.TestCase):
    """
    Test the add function from the my_math module
    """

    def test_add_integers(self):
        result = my_math.add(1, 2)
        expected = 3

        self.assertEqual(result, expected)

    def test_add_floats(self):
        result = my_math.add(10.5, 2)
        expected = 12.5
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()