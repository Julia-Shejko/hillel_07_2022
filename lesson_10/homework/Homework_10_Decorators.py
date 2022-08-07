# Створіть декоратор expected(), який перевіряє, чи те, що повертає декорована функція, має очікуваний тип.
# UnexpectedTypeException має бути викликано, якщо тип, повернутий декорованою функцією, не відповідає очікуваним.
# Вимоги:
# expected() має приймати tuple (кортеж) багатьох типів, тобто валідація повинна бути як для строки так і для інтеджера,
# якщо я передаю їх :)
# UnexpectedTypeException має бути викликано, якщо декорована функція повертає об’єкт типу, який не було визначено в
# аргументах декоратора expected()


class UnexpectedTypeException(Exception):
    pass


def expected(func):
    def wrapper(*args, **kwargs):
        implementation = func(*args, **kwargs)
        if isinstance(implementation, (int, str)):
            pass
        else:
            raise Exception("Type is not defined")
        return implementation
    return wrapper


@expected
def my_input(value):
    return value


some_input = "I can do it"
else_input = None


print(my_input(some_input))
print(my_input(else_input))
