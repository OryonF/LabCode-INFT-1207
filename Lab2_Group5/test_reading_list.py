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
        self.assertIn(["Super_Coolbros", "Nintenfake", "1991"], rows)

    def test_search_book(self):
        """Test searching for an existing book."""
        output_result = search_book("Super_Coolbros")  # Now it returns a value
        expected_output = "Found: Title: Super_Coolbros, Author: Nintenfake, Year: 1991"
        #print(f"Output: {repr(output_result)}")
        #print(f"Expected: {repr(expected_output)}")
        self.assertEqual(output_result, expected_output, "search_book did not return the expected output.")

    # More test cases to be added...


if __name__ == '__main__':
    unittest.main()