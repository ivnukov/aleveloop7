from datetime import date, timedelta


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def calculate_year_of_birth(self):
        return (date.today() - timedelta(days=self.age * 365)).year

    def change_name(self, name):
        if self.name == name:
            raise ValueError('The name is the same. Cannot change!')
        self.name = name
