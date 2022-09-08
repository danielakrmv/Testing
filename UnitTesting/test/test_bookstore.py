from unittest import TestCase, main

from project1.bookstore import Bookstore


class TestBookstore(TestCase):
    BOOK_LIMIT = 20
    INVALID_SIZE = 0

    def setUp(self) -> None:
        self.bookstore = Bookstore(self.BOOK_LIMIT)

    def test_initialization_props(self):
        self.assertEqual(self.BOOK_LIMIT, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore._Bookstore__total_sold_books)

    def test_when_books_limit_is_less_than_or_equal_zero_expect_raises(self):

        with self.assertRaises(ValueError) as error:
            Bookstore(-3)
        self.assertEqual('Books limit of -3 is not valid', str(error.exception))

    def test_when_limit_is_zero(self):
        with self.assertRaises(ValueError) as context:
            self.bookstore.books_limit = self.INVALID_SIZE

        self.assertIsNotNone(context.exception)
        self.assertEqual('Books limit of 0 is not valid', str(context.exception))
        self.assertEqual(self.BOOK_LIMIT, self.bookstore.books_limit)

    def test_increase_count_of_book(self):
        book = Bookstore(10)
        book.receive_book('Title', 5)
        self.assertEqual(1, self.bookstore.__len__())

    def test_receive_book_if_no_capacity_expect_raises(self):
        book = Bookstore(10)
        book.receive_book('Title', 5)

        with self.assertRaises(Exception) as ex:
            book.receive_book('Title', 11)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_when_title_does_not_exists(self):
        title = 'title'
        number_of_books = 5
        self.bookstore.receive_book(title, number_of_books)

        self.assertEqual(1, len(self.bookstore.availability_in_store_by_book_titles))
        self.assertTrue('title' in self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(5, self.bookstore.availability_in_store_by_book_titles[title])

    def test_receive_books_total_number_availability(self):
        title = 'title'
        number_of_books = 5

        self.assertEqual(f"5 copies of title are available in the bookstore.", self.bookstore.receive_book(title, number_of_books))

    def test_sell_book_if_title_not_available(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('Title', 4)
        self.assertEqual(f"Book Title doesn't exist!", str(ex.exception))
        self.assertTrue('Title' not in self.bookstore.availability_in_store_by_book_titles)

    def test_sell_book_expect_success(self):
        self.bookstore.receive_book('Title1', 4)
        result = self.bookstore.sell_book('Title1', 2)

        self.assertEqual(f'Sold 2 copies of Title1', result)
        self.assertEqual(2, self.bookstore.availability_in_store_by_book_titles['Title1'])
        self.assertEqual(2, self.bookstore._Bookstore__total_sold_books)

    def test_sell_book_if_we_want_to_sell_more_then_we_have(self):
        self.bookstore.receive_book('Title1', 4)

        with self.assertRaises(Exception) as ex:
            result = self.bookstore.sell_book('Title1', 5)
        self.assertEqual(f"Title1 has not enough copies to sell. Left: 4", str(ex.exception))
        self.assertTrue(4, self.bookstore.availability_in_store_by_book_titles['Title1'])
        self.assertTrue('Title1' in self.bookstore.availability_in_store_by_book_titles)

    def test_str_method(self):
        self.bookstore.receive_book('Title1', 4)
        self.bookstore.sell_book('Title1', 2)

        result = str(self.bookstore)
        expected_result = f"Total sold books: {self.bookstore._Bookstore__total_sold_books}\n" \
                          f'Current availability: 2\n' \
                          f" - Title1: 2 copies"

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()