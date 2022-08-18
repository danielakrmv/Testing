from math_op import add, divide
from unittest.mock import create_autospec

my_mocked_func = create_autospec(add, return_value='Mocking')

print(add(3, 2))

print(my_mocked_func(3, 2))

print(divide(3.0, 1))

print(my_mocked_func(1))

print(add.__doc__)
print(my_mocked_func.__doc__)