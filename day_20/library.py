
books = [] 


def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author: ")
    year = input("Enter Published Year: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "year": year
    }
    books.append(book)
    print("\n Book added successfully!\n")


def display_books():
    if not books:
        print("\n No book records found.\n")
        return
    print("\n Library Books:")
    print("-" * 50)
    for b in books:
        print(f"ID: {b['id']} | Title: {b['title']} | Author: {b['author']} | Year: {b['year']}")
    print("-" * 50)


def search_book():
    book_id = input("Enter Book ID to Search: ")
    for b in books:
        if b['id'] == book_id:
            print(f"\n🔎 Found Book: ID: {b['id']}, Title: {b['title']}, Author: {b['author']}, Year: {b['year']}\n")
            return
    print("\n Book not found.\n")


def update_book():
    book_id = input("Enter Book ID to Update: ")
    for b in books:
        if b['id'] == book_id:
            print("\nEnter new details (leave blank to keep unchanged):")
            new_title = input("New Title: ")
            new_author = input("New Author: ")
            new_year = input("New Year: ")

            if new_title:
                b['title'] = new_title
            if new_author:
                b['author'] = new_author
            if new_year:
                b['year'] = new_year

            print("\n Book updated successfully!\n")
            return
    print("\n Book not found.\n")


def delete_book():
    book_id = input("Enter Book ID to Delete: ")
    for b in books:
        if b['id'] == book_id:
            books.remove(b)
            print("\n Book deleted successfully!\n")
            return
    print("\n Book not found.\n")


def menu():
    while True:
        print("\n====== Library Management System ======")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            display_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            update_book()
        elif choice == '5':
            delete_book()
        elif choice == '6':
            print("\n Exiting... Thank you!\n")
            break
        else:
            print("\n Invalid choice! Please try again.\n")


if __name__ == "__main__":
    menu()
