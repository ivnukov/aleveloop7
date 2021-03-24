from datetime import datetime
from functools import wraps


def some_deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"func was called at {datetime.now()}")
        result = func(*args, **kwargs)
        # do something after
        result += 3
        return result

    return wrapper

@another_deco
@some_deco
def sum_two(a, b):
    return a + b


# class MyOwnList(list):
#     def __str__(self):
#         return super(MyOwnList, self).__str__().replace(',', '|')


if __name__ == '__main__':
    # print(some_deco(sum_two-func) -> wrapper(1, 7))
    # another_deco(some_deco(func))

    some_list = (x ** 2 / 15 for x in range(10))
    # some_dict = {x: y for x, y in zip([z for z in range(10)], [w for w in range(10)])}
    # some_deco(print)(12)
    # for x in range(10):
    #     some_list.append(x)
    # print(some_list)
    # print(some_dict)
    # for x in some_list:
    #     print(x)
    print(sum_two(1,2))
