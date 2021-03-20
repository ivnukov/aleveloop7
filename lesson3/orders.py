from datetime import date, timedelta

from whitespaces import main

DATABASE_URL = 'postgres://user:pass@localhost:5432'

database_url = DATABASE_URL.split(':')

SUNDAY = 7
SATURDAY = 6

WEEKEND = (SUNDAY, SATURDAY)

WORKDAYS = (x + 1 for x in range(5))


class CustomConsumer:

    def some_method(self):
        return self

    def other_method(self):
        return self


def func_first_level():
    def second_level_func():
        return 1

    return second_level_func()


temp_object = CustomConsumer()

pk = 12

user_id = 1045
record_id = 12
payment_id = 42

flag_ = 1
# user_id = 2
api_consumer = CustomConsumer()
where_to_go = False if flag_ == 1 else user_id

"""
1. WEB
    1.
2. BL
    2.1 User => User create, login, logout, change data, create ticket, cancel/delete ticket, delete account, roles
    2.2 Ticket => create, cancel/delete, approve, close, update, request info
    2.3 Ticket response => create, notify
3. DB
    3.1. User
    3.2. Ticket
    3.3. TicketResponse
    
---
1. class employee +
2. create init -> name, zp, email + 
3. def work
4. override lt,gt, gte, lte,eq, ne
5.0 setting -> 
5.1. calculate working days
# 5.1.2 get all days from 1 to current day
# 5.1.2.2 iterate over days
# 5.1.2.2.1. if weekday 6,7 || 0,6 - discard OR is holiday
5.1.2.3 return number of days
5.2. days * self.salary
"""


def calc():
    counter = 0
    today = date.today()
    first_day = date(day=1, month=today.month, year=today.year)
    while first_day <= today:
        # if first_day.isoweekday() not in WEEKEND:
        if first_day.isoweekday() in WORKDAYS:
            counter += 1
        first_day += timedelta(days=1)
    return counter


print(calc())


class Employee:
    def __init__(self, name, salary, email):
        pass

    def __lt__(self, other):
        pass
