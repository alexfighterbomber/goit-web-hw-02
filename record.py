from base_classes import *

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def find_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone:
                return ph
        return None
    
    def remove_phone(self, phone):
        ph = self.find_phone(phone)
        if ph:
            self.phones.remove(ph)
            return
        raise ValueError(f"Номер {phone} не видалено, бо не знайдено.")

    def edit_phone(self, old_phone, new_phone):
        if self.find_phone(old_phone):
            self.add_phone(new_phone)
            self.remove_phone(old_phone)
            return
        raise ValueError(f"Номер {old_phone} не знайдено.")
    
    def add_birthday(self, bd):
        self.birthday = Birthday(bd)
        

                
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"