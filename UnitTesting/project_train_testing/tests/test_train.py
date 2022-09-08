from unittest import TestCase, main

from project_library.train.train import Train


class TestTrain(TestCase):
    NAME = 'Train'
    CAPACITY = 30

    def setUp(self) -> None:
        self.train = Train(self.NAME, self.CAPACITY)

    def test_initialization_params(self):
        self.assertEqual(self.NAME, self.train.name)
        self.assertEqual(self.CAPACITY, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_passengers_if_no_capacity_expect_raises(self):
        train = Train(self.NAME, 2)

        train.passengers.append('Ivan')
        train.passengers.append('Gosho')

        with self.assertRaises(ValueError) as error:
            train.add('Joro')
        self.assertEqual("Train is full", str(error.exception))
        self.assertTrue('Ivan' in train.passengers)
        self.assertTrue('Gosho' in train.passengers)

    def test_add_passenger_if_he_already_exists_expect_raises(self):
        self.train.passengers.append('Ivan')

        with self.assertRaises(ValueError) as error:
            self.train.add('Ivan')
        self.assertEqual("Passenger Ivan Exists", str(error.exception))
        self.assertTrue('Ivan' in self.train.passengers)

    def test_add_passenger_if_we_have_capacity_and_passenger_not_in_the_train_yet(self):
        train = Train(self.NAME, 2)

        train.passengers.append('Ivan')

        result = train.add('Gosho')
        self.assertEqual("Added passenger Gosho", result)
        self.assertTrue('Gosho' in train.passengers)
        self.assertTrue('Ivan' in train.passengers)

    def test_remove_passenger_if_he_does_not_present_in_passengers_list_expect_raises(self):
        train = Train(self.NAME, 2)

        train.passengers.append('Ivan')

        with self.assertRaises(ValueError) as error:
            train.remove('Georgi')
        self.assertEqual("Passenger Not Found", str(error.exception))
        self.assertTrue('Ivan' in train.passengers)

    def test_if_we_successfully_remove_passenger(self):
        train = Train(self.NAME, 2)

        train.passengers.append('Ivan')

        result = train.remove('Ivan')

        self.assertEqual("Removed Ivan", result)
        self.assertTrue('Ivan' not in train.passengers)


if __name__ == '__main__':
    main()