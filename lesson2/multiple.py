class Parent:

    def __init__(self, age, gender, name, dob):
        self.age = age
        self.gender = gender
        self.name = name
        self.dob = dob

    def iam(self):
        return f"I am {self.__class__.__name__} and {self.age} yo"

    def working(self):
        return 'I\'m working'


class GrandParent:

    def iam(self):
        return "Molodezh Poshla"


class Child(Parent, GrandParent):
    def __init__(self, has_mobile, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.has_mobile = has_mobile

    def iam(self):
        parent_iam = super().iam()
        return parent_iam + ". I'm not a parent, lol"


class Rectangle:
    def __init__(self, length, height):
        self.length = length
        self.height = height


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


if __name__ == '__main__':
    # p = Parent(21, 'F', 'Natasha', '01/02/2000')
    # print(p.__dict__)
    # print(p.iam())
    c = Child(True, 21, 'F', 'Natasha', '01/02/2000')
    print(c)
    print(Child.__mro__)
    print(c.iam())
    print(c.working())
    print(c.age)

    rect = Rectangle(length=12, height=5)
    sq = Square(length=14)
    print(rect.__dict__)
    print(sq.__dict__)
