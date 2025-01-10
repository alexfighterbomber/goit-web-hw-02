from abc import ABC, abstractmethod
import pickle

from base_classes import *
from record import *
from address_book import *
from input import *



def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено


# Абстрактний базовий класс для користувальницьких уявлень
class UserView(ABC):
    @abstractmethod
    def show_message(self, message: str):
        pass

    @abstractmethod
    def show_commands(self):
        pass

# Конкретний класс для консольного інтерфейсу
class ConsoleUserView(UserView):
    def show_message(self, message: str):
        print(message)

    def show_commands(self):
        commands = [
            "hello - вітання",
            "add <name> <phone> - додати контакт",
            "del <name> - видалити контакт",
            "change <name> <old_phone> <new_phone> - змінити телефон",
            "phone <name> - показати телефони",
            "all - показати всі контакти",
            "add-birthday <name> <birthday> - додати день нарождення",
            "show-birthday <name> - показати день нарождення",
            "birthdays - показать найближчі дні нарождення",
            "close/exit - вийти"
        ]
        print("Доступні команди:")
        for cmd in commands:
            print(f"  {cmd}")



def main():
    book = load_data()
    view = ConsoleUserView()  # Ініціалізуємо консольное відображення
    view.show_message("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
            view.show_message("Good bye!")
            break

        elif command == "hello":
            view.show_message("How can I help you?")
            
        elif command == "add":
            view.show_message(add_contact(args, book))

        elif command == "del":
            view.show_message(del_contact(args, book))
            
        elif command == "change":
            view.show_message(change_contact(args, book))
            
        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            view.show_message(show_all(book))

        elif command == "add-birthday":
            view.show_message(add_birthday(args, book))
            
        elif command == "show-birthday":
            view.show_message(show_birthday(args, book))

        elif command == "birthdays":
            view.show_message(birthdays(book))

        elif command in ["help", "?"]:
            view.show_commands()

        else:
            view.show_message("Invalid command.")
            pass




if __name__ == "__main__":
    main()
