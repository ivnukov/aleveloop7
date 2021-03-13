from datetime import datetime
from random import choice


class Human:
    def __new__(cls, *args, **kwargs):
        print(datetime.now())
        return object.__new__(cls)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __del__(self):
        print('I see the light.')

    def __str__(self):
        return f"{self.__repr__()} | name: {self.name}"

    def __call__(self, food):
        print(f'I\'m eating {food}')

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return self.age != other.age

    def __add__(self, other):
        gender = choice([self.gender, other.gender])
        name = self.name + other.name
        age = 0
        return Human(name, age, gender)

    def __bool__(self):
        return self.gender == 'F'

    def __getitem__(self, item):
        return getattr(self, item, 42)


if __name__ == '__main__':
    vasya = Human(name='Vasya', age=30, gender='M')
    vasya2 = Human(name='Vasya', age=30, gender='M')
    marina = Human('Marina', age=64, gender='F')
    print(vasya)
    print(vasya2)
    print(marina)

    vasya('makaroshki')

    print(vasya > marina)
    print(vasya >= marina)
    print(vasya < marina)
    print(vasya <= marina)
    print(vasya == marina)
    print(vasya != marina)

    child = vasya + marina
    print(child.__dict__)

    print(bool(vasya))
    print(bool(marina))

    print(marina['age'])
    print(marina['qwe'])

    print(dir('marina'))