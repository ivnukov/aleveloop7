# import models
#
# recruiter = models.Recruiter('Abba', 23, '2123123')

def magic_func(arg=None):
    print(arg)


def main():
    a = 1 + 2
    b = a - -2  # * / // %
    print(a < b)  # <= < > >= == !=
    magic_func(arg='Hello world!')


if __name__ == '__main__':
    main()
