"""
Створіть декоратор expected(), який перевіряє, чи те, що повертає декорована функція, має очікуваний тип.
UnexpectedTypeException має бути викликано, якщо тип, повернутий декорованою функцією, не відповідає очікуваним.
Вимоги:
expected() має приймати tuple (кортеж) багатьох типів, тобто валідація повинна бути як для строки так і для інтеджера,
якщо я передаю їх :)
UnexpectedTypeException має бути викликано, якщо декорована функція повертає об’єкт типу, який не було визначено в
аргументах декоратора expected()

"""

import functools

class UnexpectedTypeException(Exception):
    pass


def expected(type):

    def expected_type(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            implementation = func(*args, **kwargs)
            if not isinstance(implementation, type):
                raise Exception("Type is not defined")
            return implementation

        return wrapper

    return expected_type


@expected(type=(str, int))
def my_input(value):
    return value


print(my_input("I can do it"))
print(my_input(None))
