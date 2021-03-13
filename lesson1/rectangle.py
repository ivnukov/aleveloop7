from time import sleep

print(__name__)


class Rectangle:
    def __init__(self, height, length):
        self.height = height
        self.length = length

    def __str__(self):
        return f"Rectangle with {self.height} {self.length}"

    def square(self):
        return self.height * self.length

    def perimeter(self):
        print(self)
        return (self.height + self.length) * 2

    def is_square(self):
        print(self)
        return self.height == self.length

    def run(self):
        sleep(5)


if __name__ == '__main__':
    Rectangle(1, 2).run()
