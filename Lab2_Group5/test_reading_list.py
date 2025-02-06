import csv
import unittest
from Lab2_Oryon_Jayce import add_book, list_books, search_book


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

    # More test cases to be added...
    def test_list_books(self):
        filler = ""

    def test_delete_books(self):
        filler = ""



if __name__ == '__main__':
    unittest.main()