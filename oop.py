# oop
# Create a class called Car with attributes brand and color. Instantiate an
#  object of the Car class and print its attributes.#Add a method called start_engine to the Car class that prints a
#  message saying the engine of the car has started. Create an
#  instance of Car and call the method.
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
       print(f"The engine of the {self.color}{self.brand} has started.") 

my_car = Car("Mercedes", "Black")
print("Brand:", my_car.brand)
print("Color:", my_car.color) 

my_car.start_engine()


#Add a method called start_engine to the Car class that prints a
#  message saying the engine of the car has started. Create an
#  instance of Car and call the method.
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
       print(f"The engine of the {self.color} {self.brand} has started.") 
my_car.start_engine()


# Create a class called BankAccount with attributes account_number and balance. Add methods to:
#Deposit an amount.
#Withdraw an amount (only if sufficient balance exists).
#Print the account balance.
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")

            return
        self.balance += amount
        print(f"Deposited {amount} to account {self.account_number}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")

            return
        if amount > self.balance:
            print(f"Insufficient balance to withdraw {amount} from account {self.account_number}.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")

    def print_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")


account = BankAccount("12345678", initial_balance=1000)
account.deposit(2000)
account.print_balance()
account.withdraw(2000)
account.print_balance()
account.withdraw(1000)
account.print_balance()
account.deposit(0)
account.withdraw(700)


#: Implement a class called Library that manages a collection of books.
#  Each book has a title, author, and available status. The Library class should have methods to:
#Add a book to the library.
#Remove a book from the library.
#Check if a book is available by title.
#Borrow a book (mark it as unavailable if it’s available).
#Return a book (mark it as available again if it was borrowed).  # 
                       
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        return f"'{self.title}' by {self.author} ({'Available' if self.is_available else 'Unavailable'})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"The book '{title}' by {author} was added to the library.")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"The book'{title}' was removed from the library.")
                return
        print(f"The book '{title}' was not found in the library.")

    def check_availability(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book.is_available
        print(f"Book '{title}' not found in the library.")
        return False

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_available:
                    book.is_available = False
                    print(f"You have borrowed '{title}'.")
                else:
                    print(f"Book '{title}' is currently unavailable.")
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_available:
                    book.is_available = True
                    print(f"Book '{title}' has been returned.")
                else:
                    print(f"Book '{title}' was not borrowed.")
                return
        print(f"Book '{title}' not found in the library.")

    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)


library = Library()
library.add_book("From the depths", "Anna Grace")
library.add_book("Bruises", "Daina Flair")
library.list_books()
print("\n")

library.check_availability("Bruises")
library.borrow_book("Bruises")
library.check_availability("Bruises")
library.return_book("Bruises")
library.remove_book("From the depths")
library.list_books()
