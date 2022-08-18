from unittest.mock import Mock


my_mock = Mock()
print(type(my_mock))


print(my_mock)
my_mock = Mock(return_value="my_mock object")
print(str(my_mock))

my_mock.__str__ = "I'm changing you!"
my_mock.__str__ = Mock(return_value='__str__ I mock you!')
print(my_mock)

my_mock_function = Mock(return_value="My real mock function")

my_mock.return_value = 'Daniela'
print(my_mock.return_value)

print(my_mock.called)

my_mock()
print(my_mock.called)

mock = Mock()
mock.name = 'Daniela'
print(mock.name)

import datetime

# Save a couple of test days
tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

# Mock datetime to control today's date
datetime = Mock()

def is_weekday():
    today = datetime.datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return (0 <= today.weekday() < 5)

# Mock .today() to return Tuesday
datetime.datetime.today.return_value = tuesday
# Test Tuesday is a weekday
assert is_weekday()
# Mock .today() to return Saturday
datetime.datetime.today.return_value = saturday
# Test Saturday is not a weekday
assert not is_weekday()



