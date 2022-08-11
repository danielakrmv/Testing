from UnitTesting import math_operations
from unittest import TestCase, main


class TestAdd(TestCase):

    def test_add_func_integers(self):
        result = math_operations.add(2, 3)
        self.assertEqual(5, result) # expected_info, actual_info

    def test_add_func_floats(self):
        result = math_operations.add(4.5, 6.7)
        self.assertEqual(11.2, result)

    def test_add_func_string(self):
        result = math_operations.add('h', 'i')
        self.assertEqual('hi', result)

    def test_add_func_string_and_num_expect_raises(self):
        with self.assertRaises(TypeError) as er:
            math_operations.add(1, 'Daniela')
        self.assertEqual("unsupported operand type(s) for +: 'int' and 'str'", str(er.exception))


class TestSubtract(TestCase):

    def test_subtract_func_integers(self):
        result = math_operations.subtract(6, 5)
        self.assertEqual(1, result)  # expected_info, actual_info

    def test_subtract_func_floats(self):
        result = math_operations.subtract(3.5, 1.5)
        self.assertEqual(2.0, result)

    def test_subtract_func_strings_expect_raises(self):
        with self.assertRaises(TypeError) as er:
            math_operations.subtract("hi", "Daniela")
        self.assertEqual("unsupported operand type(s) for -: 'str' and 'str'", str(er.exception))

    def test_subtract_func_strings_and_integer_expect_raises(self):
        with self.assertRaises(TypeError) as er:
            math_operations.subtract(1, "hi")
        self.assertEqual("unsupported operand type(s) for -: 'int' and 'str'", str(er.exception))


class TestMultiply(TestCase):

    def test_multiply_func_integers(self):
        result = math_operations.multiply(6, 5)
        self.assertEqual(30, result)  # expected_info, actual_info

    def test_multiply_func_floats(self):
        result = math_operations.multiply(3.5, 1.2)
        self.assertEqual(4.2, result)

    def test_multiply_func_strings_integers(self):
        result = math_operations.multiply('d', 3)
        self.assertEqual('ddd', result)

    def test_multiply_func_strings_expect_raises(self):
        with self.assertRaises(TypeError) as er:
            math_operations.multiply("hi", "Daniela")
        self.assertEqual("can't multiply sequence by non-int of type 'str'", str(er.exception))


class TestDivision(TestCase):
    def test_division_func_integers(self):
        result = math_operations.divide(9.0, 3)
        self.assertEqual(3.0, result)  # expected_info, actual_info

    def test_division_func_by_zero_expect_raises(self):
        with self.assertRaises(ZeroDivisionError) as er:
            math_operations.divide(9.0, 0)
        self.assertEqual("float division by zero", str(er.exception))


    def test_division_func_strings_expect_raises(self):
        with self.assertRaises(ValueError) as er:
            math_operations.divide("hi", "Daniela")
        self.assertEqual("could not convert string to float: 'hi'", str(er.exception))

    def test_division_func_floats(self):
        result = math_operations.divide(9.0, 4.5)
        self.assertEqual(2.0, result)


if __name__ == "__main__":
    main()

