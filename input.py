from record import *

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command"
        except KeyError:
            return "Key not found. Please enter a valid name."

    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        try:
            record.add_phone(phone)
        except ValueError as e:
            return e
    return message

@input_error
def del_contact(args, book):
    name = args[0]
    try:
        book.delete(name)
    except Exception as e:
        return e
    return f"Contact {name} delete."


@input_error
def change_contact(args, book):
    name, old_phone, new_phone = args # Считываем первые три элемента из списка args
    record = book.find(name)
    if record:
        if old_phone and new_phone:  # если есть все данные
            try:
                record.edit_phone(old_phone, new_phone)
            except ValueError as e:
                return e
            return "Phone updated." 
        else: return 'Use the format: Name  old_phone  new_phone'
    else: return no_one()

@input_error
def show_phone(args, book):
    name = args[0]  # Считываем первый элемент из списка args
    record = book.find(name)
    if record is None:
        return no_one()
    return f'{record.name.value} phones: {"; ".join(phone.value for phone in record.phones)}'
    
@input_error
def show_all(book):
    if not book.data:
        return no_one()
    ret_str = ""
    for record in book.data.values():  # book.data содержит записи
        birthday =  record.birthday.value if record.birthday else None
        phones = "; ".join(phone.value for phone in record.phones) if record.phones else "no phones"
        if birthday:
            ret_str += f"Name: {record.name.value} Phones: {phones} Birthday: {birthday}\n"
        else:
            ret_str += f"Name: {record.name.value} Phones: {phones}\n"

    return ret_str.rstrip()

@input_error
def add_birthday(args, book):
    name, birthday = args # Считываем первые 2 элемента из списка args
    record = book.find(name)   
    if record is None:
        return no_one()
    if birthday:
        try:
            record.add_birthday(birthday)
        except ValueError as e:
            return e
    return f"{name}\'s birthday added"

@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)   
    if record is None:
        return no_one()
    return record.birthday

@input_error
def birthdays(book):
    out_str = '\nCongratulation days:\n--------------------\n'
    sorted_birthdays = book.get_upcoming_birthdays()
    if not sorted_birthdays: return f'No birthdays in the next 7 days'
    for person in sorted_birthdays:
        name = person.get('name')
        birthday = person.get('birthday')
        out_str += f'{name} - {birthday}\n'
    return out_str
 
def no_one():
    return "Такий тут не живе!"  # Возвращаем  ошибку