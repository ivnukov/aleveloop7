class Rectangle:
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'R: {self.length}X{self.height}'

    @property
    def square(self):
        return self.height * self.length

    @staticmethod
    def to_inches(value):
        return value / 2.54

    def to_string(self, system_='M'):
        if system_ == 'M':
            return f"Rectange {self.height}X{self.length}"
        elif system_ == 'B':
            return f"Rectangle {self.to_inches(self.length)} X {self.to_inches(self.height)}"
        raise ValueError('invalid system')

    @classmethod
    def from_txt(cls, fp):
        result = []
        with open(fp) as data_file:
            for row in data_file:
                sizes = row.split(',')
                result.append(cls(int(sizes[0]), int(sizes[1])))
        return result

    @classmethod
    def get_user_by_id(cls, id):
        query = f"select * from users where id = {id}"
        result = conn.execute(query)
        return cls(**result)

    @classmethod
    def get_all_active_user(cls):
        query = f"select * from users where status = 'active'"
        result = conn.execute(query)
        return (cls(**x) for x in result)


if __name__ == '__main__':
    rectangles = Rectangle.from_txt('rectangle')
    print(rectangles)
    print([x.square for x in rectangles])

    user = Rectangle.get_user_by_id(12)
