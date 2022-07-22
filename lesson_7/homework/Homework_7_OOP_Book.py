# Завдання 2
# Реалізуйте клас «Book».
# Необхідно зберігати в полях класу: назву книги, рік випуску, видавництва, жанр, автора, ціну.
# Реалізуйте методи класу для введення даних, виведення даних, реалізуйте доступ до окремих полів через методи класу.

class Book:
    def __init__(self, name, year, publishing_house, genre, author, price):
        self.name = name
        self.year = year
        self.publishing_house = publishing_house
        self.genre = genre
        self.author = author
        self.price = price

    def show_details(self):
        message = "This is a book."
        print(
            f'{message} Name: {self.name}\nYear of publication: {self.year}\nPublishing_house: {self.publishing_house}'
            f'\nGenre: {self.genre}\nAuthor: {self.author}\nPrice: {self.price} $')

    def get_name(self):
        print(f"The book title is: '{self.name}'")

    def get_year(self):
        print(f"{self.year} is the year of publication of this book")

    def get_publishing_house(self):
        print(f"{self.publishing_house} published this book")

    def get_genre(self):
        print(f"This book belongs to the {self.genre} genre")

    def get_author(self):
        print(f"{self.author} wrote this book")

    def get_price(self):
        print(f"This book costs {self.price} $")


first_book = Book(
    name = "The Gift",
    year = 2021,
    publishing_house = "Rider & Co",
    genre = "Modern literature",
    author = "Edith Eva Eger",
    price = 10)

first_book.show_details()
first_book.get_name()
first_book.get_year()
first_book.get_publishing_house()
first_book.get_genre()
first_book.get_author()
first_book.get_price()
