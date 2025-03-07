"""Home work 1"""

from abc import ABC, abstractmethod
import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.DEBUG,
    handlers=[logging.StreamHandler()],
)


class Author:
    """Author information for library"""

    def __init__(self, name: str):
        self.name = name


class Book:
    """Book information"""

    def __init__(self, title: str, year: int, author: Author):
        self.title = title
        self.year = year
        self.author = author


class LibraryInterface(ABC):
    """Library Base Interface"""

    @abstractmethod
    def add_book(self, book: Book) -> None:
        """Adding new book to items"""

    @abstractmethod
    def remove_book(self, book: Book) -> None:
        """Remove book by title"""

    @abstractmethod
    def get_books(
        self,
    ) -> list[Book]:
        """Return list of books"""


class Library(LibraryInterface):
    """The Library class"""

    def __init__(self):
        self.books = []

    def add_book(self, book: Book) -> None:
        """Add new book to lib"""
        self.books.append(book)

    def remove_book(self, book: Book) -> None:
        """Remove book from lib"""
        self.books.remove(book)

    def get_books(self) -> list[Book]:
        """Return all books"""
        return self.books


class LibraryManager:
    """Class for manageing lib"""

    def __init__(self, library: Library):
        self.library = library

    def add_new_book(self, title: str, year: int, author_name: str):
        """Add new book to library"""
        author = Author(author_name)
        book = Book(title, year, author)
        self.library.add_book(book)

    def remove_book_by_title(self, title: str) -> None:
        """Remove book from lib"""
        for book in self.library.books:
            if book.title == title:
                self.library.remove_book(book)
                logging.info("Book '%s' successfully removed", title)
                return
        logging.warning("Book '%s' not found", title)

    def show_books(self) -> None:
        """Show all books in lib"""
        books = self.library.get_books()
        if not books:
            logging.warning("Books was not found.")
            return
        for book in books:
            logging.info(
                "Title: %s, Author: %s, Year: %s",
                book.title,
                book.author.name,
                book.year,
            )


def main():
    """Main program"""
    library = Library()
    manager = LibraryManager(library)
    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        if command == "add":
            title = input("Enter book title: ").strip()
            author_name = input("Enter book author: ").strip()
            year = int(input("Enter book year: ").strip())
            manager.add_new_book(title, year, author_name)
        elif command == "remove":
            title = input("Enter book title to remove: ").strip()
            manager.remove_book_by_title(title)
        elif command == "show":
            manager.show_books()
        elif command == "exit":
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
