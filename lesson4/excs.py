import traceback


class MySuperExceptionException(Exception):
    pass

    def __init__(self):
        pass

    def dump_to_string(self):
        pass


class MyAwesomeError(MySuperExceptionException):
    pass


def main_first():
    a = 6
    b = 3
    result = a / b
    assert (result == 2)

    # print(a.c)
    # try:
    #     a$w
    # except SyntaxError:
    #     print('I tak soidet!')

    # for a in range(3):
    # print(a)


def divide(a, b):
    # try:
    return a / b
    # except ZeroDivisionError:
    #     return "Can't divide by zer0"


if __name__ == '__main__':
    # a = MySuperExceptionException()
    # print(isinstance(a, MySuperExceptionException))

    try:
        first = int(input('Enter the first number: \n'), 10)
        second = int(input('Enter the second number: \n'), 10)
        result = divide(first, second)
    except (ValueError  , TypeError) as err:
        second = 1
        print("Input is wrong")
        # err.some_method()
        # a = traceback.format_exc()
        # print(a)
    # except ArithmeticError:
    #     pass
    # else:
    #     print('Molodec! Pryam dva chisla vvel!')
    finally:
        print("Im in finally!")

    # print(f'Result is {divide(first, second)}.')
