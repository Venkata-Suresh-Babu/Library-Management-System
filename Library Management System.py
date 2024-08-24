class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = True

    def display_details(self):
        print(f"{self.title} by {self.author} ({self.genre})")

    def update_availability(self, status):
        self.available = status

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_title(self, title):
        for book in self.books:
            if title.lower() in book.title.lower():
                book.display_details()


if __name__ == "__main__":
    my_library = Library()

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")

    my_library.add_book(book1)
    my_library.add_book(book2)

    my_library.search_by_title("Gatsby")