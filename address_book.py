from collections import UserDict
from datetime import date, timedelta

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError(f"Запис з ім'ям {name} не знайдено.")

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
    
    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays = []
        today = date.today()
        for record in self.data.values():
            if record.birthday:
                bd_date = record.birthday.bd_date()
                birthday_this_year = bd_date.replace(year=today.year)
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                days_until_birthday = (birthday_this_year - today).days
                if 0 <= days_until_birthday <= days:
                    congratulation_date = self.adjust_for_weekend(birthday_this_year)
                    upcoming_birthdays.append({
                        "name": record.name.value,
                        "birthday": congratulation_date
                    })
        bd_sort = sorted(upcoming_birthdays, key=lambda x: x["birthday"])
        return [{'name': item['name'], 'birthday': item['birthday'].strftime('%d.%m.%y')} for item in bd_sort]

    
    def find_next_weekday(self, start_date, weekday):
        start_weekday = start_date.weekday()
        if  start_weekday >= weekday : weekday += 7
        return start_date + timedelta(days = weekday - start_weekday)

    def adjust_for_weekend(self, birthday):
        if birthday.weekday() >= 5: birthday = self.find_next_weekday(birthday, 0)
        return birthday
