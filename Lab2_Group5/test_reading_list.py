import csv
import unittest
from Lab2_Oryon_Jayce import add_book, list_books, search_book, delete_book


class TestReadingList(unittest.TestCase):
    def test_add_book(self):
        # Test adding a book
        add_book("Super_Coolbros", "Nintenfake", 1991)
        with open("books.csv", "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
        # important to know that when the data has been entered in the csv file
        # it becomes a string regards of it's past data type.
        self.assertIn(["Super_Coolbros", "Nintenfake", "1991"], rows)

    def test_search_book(self):
        """Test searching for an existing book."""
        output_result = search_book("Super_Coolbros")  # Now it returns a value
        expected_output = "Found: Title: Super_Coolbros, Author: Nintenfake, Year: 1991"
        self.assertEqual(output_result, expected_output, "search_book did not return the expected output.")

    def test_list_books(self):
        add_book("Oryx and Crake", "Margaret Atwood", 2003)
        result = search_book("Oryx and Crake")
        self.assertEqual(result, "Found: Title: Oryx and Crake, Author: Margaret Atwood, Year: 2003")

    def test_delete_books(self):
        add_book("Delete me", "Test author", 2025)
        delete_book("Delete me")
        result = search_book("Delete me")
        self.assertEqual(result, "Book not found")

    def test_null_title(self):
        add_book("", "test null title", 2025)
        result = search_book("")
        self.assertEqual(result, "Book not found")

    def test_null_author(self):
        add_book("test null author", "", 2025)
        result = search_book("test null author")
        self.assertEqual(result, "Book not found")

    def test_null_year(self):
        add_book("test null year", "test null year author", "")
        result = search_book("test null year")
        self.assertEqual(result, "Book not found")

    def test_year_not_numeric(self):
        add_book("test alpha year", "test alpha year author", "year")
        result = search_book("test alpha year")
        self.assertEqual(result, "Book not found")

    def test_year_high(self):
        add_book("test year too high", "year too high author", 2026)
        result = search_book("test year too high")
        self.assertEqual(result, "Book not found")

    def test_year_low(self):
        add_book("test year too low", "year too low author", -500)
        result = search_book("test year too low")
        self.assertEqual(result, "Book not found")


if __name__ == '__main__':
    unittest.main()