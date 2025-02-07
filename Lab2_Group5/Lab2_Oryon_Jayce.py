##################################################################
# Program:          Lab 2 - Book List
# Authors:          Jayce Johnson and Oryon Facey
# Date:             February 7th, 2025
# Description:      Allows the user to add, list, and delete books 
#                   from a CSV file.
##################################################################

import csv

# Function to add a book to the reading list
def add_book(title, author, year):

    # Validating that the year is a number
    try:
        year = int(year)
    except:
        print("Year must be a digit.")

    # Validating that the year makes sense (book published between year 1 and 2025)
    if year > 2025 or year < 1:
        print("Please enter a valid year.")

    # If validation passes, adds to csv
    else:
        with open("books.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([title, author, year])

# Function to list all books
def list_books():
    # We are going to make an array of books for the books list in
    # books.csv
    books = []
    with open("books.csv", mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            books.append(f'Title: {row[0]}, Author: {row[1]}, Year: {row[2]}')
    return "\n".join(books)


# Function to search for a book by title
def search_book(title):
    with open("books.csv", mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].lower() == title.lower():
                # returns the f string, this is important to make the
                # testing work because the print method does not return a
                # value it only displays a message.
                return f'Found: Title: {row[0]}, Author: {row[1]}, Year: {row[2]}'
        return 'Book not found'

# We need a delete book function
def delete_book(title):

    book_found = False

    # Read all books except the one to be deleted
    with open("books.csv", mode="r") as file:
        reader = csv.reader(file)
        # Makes a new list called books that will copy the contents of
        # books.csv except for the title the user wishes to delete.
        # Also row[0].lower() != title.lower() makes it not case
        # sensitive.
        books = []
        for row in reader:
            if row[0].lower() == title.lower():
                book_found = True
            else:
                books.append(row)

    # Write back only the books that were not deleted
    with open("books.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(books)

    if book_found == True:
        return f"{title} has been deleted."
    else:
        return "Book not found. No records deleted."

# Menu loop
def menu():
    while True:
        print("\n1. Add Book\n2. List Books\n3. Search Book\n4. Delete Book "
              "\n5. Quit")
        choice = input("Select an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = input("Enter year of publication: ")
            add_book(title, author, year)
        elif choice == '2':
            print(list_books())
        elif choice == '3':
            title = input("Enter book title to search: ")
            print(search_book(title))
        elif choice == '4':
            title = input("Enter book title to search: ")
            print(delete_book(title))
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    menu()
