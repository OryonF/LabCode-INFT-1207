import csv


# Function to add a book to the reading list
def add_book(title, author, year):
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

    # Read all books except the one to be deleted
    with open("books.csv", mode="r") as file:
        reader = csv.reader(file)
        # Makes a new list called books that will copy the contents of
        # books.csv except for the title the user wishes to delete.
        # Also row[0].lower() != title.lower() makes it not case
        # sensitive.
        books = [row for row in reader if row and row[0].lower() != title.lower()]

    # Write back only the books that were not deleted
    with open("books.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(books)

    print(f'Book "{title}" has been deleted (if it existed).')

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
            delete_book(title)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    menu()
