class Library:
    def __init__(self, books):
        self.books = books  
        self.borrowed = {}  

    def show_books(self):
        if self.books:
            print("\n Available Books:")
            for book in self.books:
                print(" -", book)
        else:
            print("\n No books available right now.")

    def borrow_book(self, user, book):
        if book in self.books:
            self.books.remove(book)
            self.borrowed.setdefault(user, []).append(book)
            print(f" {user} borrowed '{book}'")
        else:
            print(f" Sorry, '{book}' is not available.")

    def return_book(self, user, book):
        if user in self.borrowed and book in self.borrowed[user]:
            self.borrowed[user].remove(book)
            self.books.append(book)
            print(f" {user} returned '{book}'")
        else:
            print(f" {user} did not borrow '{book}'")


library = Library(["Python Basics", "Data Science 101", "AI for Beginners"])

library.show_books()

library.borrow_book("Prajwal", "Python Basics")
library.borrow_book("Ravi", "AI for Beginners")
library.show_books()

library.return_book("Prajwal", "Python Basics")
library.show_books()
