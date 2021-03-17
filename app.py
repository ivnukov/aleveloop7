from lesson2.dunder import Human
from lesson1.rectangle import Rectangle
from lesson3.orders import CustomConsumer

print(__name__)

if __name__ == '__main__':
    figure_1 = Rectangle(3, 10)
    figure_2 = Rectangle(5, 5)

    print(figure_1.is_square())
    print(figure_1.perimeter())
    print(figure_2.is_square())

    # a = Human()
    cons = CustomConsumer()
