class Book:
    def __init__(self, title, author, isbn):
        self.__title = title  
        self.__author = author  
        self.__isbn = isbn  
        self.__is_checked_out = False  

    def get_details(self):
        return {
            "title": self.__title,
            "author": self.__author,
            "isbn": self.__isbn,
            "is_checked_out": self.__is_checked_out
        }

    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False


class Library:
    def __init__(self):
        self.__books = []  

    def add_book(self, book):
        if len(self.__books) < 8:  
            self.__books.append(book)
        else:
            print("Library is full. Cannot add more books.")

    def find_book(self, isbn):
        for book in self.__books:
            if book.get_details()["isbn"] == isbn:
                return book
        return None

    def list_books(self):
        return [book.get_details() for book in self.__books]


class Member:
    def __init__(self, name, member_id):
        self.__name = name  
        self.__member_id = member_id  
        self.__borrowed_books = []  


    def get_details(self):
        return {
            "name": self.__name,
            "member_id": self.__member_id,
            "borrowed_books": [book.get_details() for book in self.__borrowed_books]
        }

    def borrow_book(self, book):
        if book.check_out():
            self.__borrowed_books.append(book)
            print(f"{self.__name} borrowed '{book.get_details()['title']}'.")
        else:
            print(f"'{book.get_details()['title']}' is already checked out.")

    def return_book(self, book):
        if book in self.__borrowed_books and book.return_book():
            self.__borrowed_books.remove(book)
            print(f"{self.__name} returned '{book.get_details()['title']}'.")
        else:
            print(f"{self.__name} cannot return '{book.get_details()['title']}'.")



if __name__ == "__main__":

    library = Library()

    books = [
        Book("Noli Me Tangere", "Dr. José Rizal", "9780143039693"),
        Book("El Filibusterismo ", "Dr. José Rizal", "9780143106395"),
        Book("Florante at Laura ", "Francisco Balagtas", "9788888976280"),
        Book("Moby Dick", "Herman Melville", "2233445566"),
        Book("Dekada '70 ", "Lualhati Bautista", "9789711790233"),
        Book("Pride and Prejudice", "Jane Austen", "4455667788"),
        Book("Alamat ng Gubat ", "Bob Ong", "9789719257417"),
        Book("The Hobbit", "J.R.R. Tolkien", "6677889900"),
    ]

    for book in books:
        library.add_book(book)

    print("Books in the library:")
    for book in library.list_books():
        print(book)

    member = Member("Ryan Kenneth", "M001")

    member.borrow_book(library.find_book("9780143039693"))  
    member.borrow_book(library.find_book("9789719257417"))  
    member.borrow_book(library.find_book("2233445566")) 