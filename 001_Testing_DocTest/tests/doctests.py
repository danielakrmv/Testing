def add(a, b):
    """
    Return the addition of the arguments: a + b
    :param a: int a number
    :param b: int b number
    :return: the result of addition of a and b


    >>> add(2, 3)
    5
    >>> add(-2, 3)
    1
    >>> add(4.5, 6.7)
    11.2
    >>> add("h", "i")
    'hi'
    >>> add(1, "Daniela")
    Traceback (most recent call last):
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return a + b


def subtract(a, b):
    """
    Return the subtraction of the arguments: a - b
    :param a: int a number
    :param b: int b number
    :return: the result of subtraction of a and b


    >>> subtract(6, 5)
    1
    >>> subtract(-3, 4)
    -7
    >>> subtract(-3, -4)
    1
    >>> subtract(3.5, 1.5)
    2.0
    >>> subtract("hi", "Daniela")
    Traceback (most recent call last):
    TypeError: unsupported operand type(s) for -: 'str' and 'str'
    >>> subtract(3, "hi")
    Traceback (most recent call last):
    TypeError: unsupported operand type(s) for -: 'int' and 'str'
    """
    return a - b


def multiply(a, b):
    """
    Return the subtraction of the arguments: a * b
    :param a: int a number
    :param b: int b number
    :return: the result of multiplication of a and b


    >>> multiply(5, 6)
    30
    >>> multiply('d', 3)
    'ddd'
    >>> multiply(3, -4)
    -12
    >>> multiply(3.5, 1.2)
    4.2
    >>> multiply('h', 'd')
    Traceback (most recent call last):
    TypeError: can't multiply sequence by non-int of type 'str'
    """
    return a * b


def division(numerator, denominator):
    """
    Return the devision of the arguments numerator / denominator
    :param numerator: float numerator number
    :param denominator: int denominator number
    :return: float the result of division of numerator and denominator


    >>> division(9.0, 3)
    3.0
    >>> division(9.0, 0)
    Traceback (most recent call last):
    ZeroDivisionError: float division by zero
    >>> division("Hi", "Daniela")
    Traceback (most recent call last):
    TypeError: unsupported operand type(s) for /: 'str' and 'str'
    >>> division(9.0, 4.5)
    2.0
    """
    return numerator / denominator


if __name__ == "__main__":
    import doctest
    doctest.testmod()

