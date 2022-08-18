from unittest import mock

import random


def roll_dice():
    print("rolling...")
    return random.randint(1, 6)


roll_dice()
# mock_roll_dice = mock.Mock()
# <Mock id='2946665821616'>
# print(mock_roll_dice())
# <Mock name='mock()' id='1805483130064'>


mock_roll_dice = mock.Mock(name='roll dice mock', return_value=3)
print(mock_roll_dice)
# 3
roll_dice = mock_roll_dice
print(roll_dice())
# rolling...
# <Mock name='roll dice mock' id='2242597893552'>
# 3


