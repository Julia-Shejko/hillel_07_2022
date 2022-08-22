"""
 - Коли додаток запускається, три потоки (T1, T2, T3) стартують
    - потік T1 заповнює список випадковими числами (10_000 елементів)
    - потоки T2 та T3 очікують, доки попередній список заповниться
    - коли список заповнений, T2 та T3 стартують
    - потік T2 знаходить суму елементів у списку
    - потік T3 знаходить середнє арифметичне для елементів у списку
    - на екран виводяться результуючі 2 списки (2 список - вихідні дані з T2 та T3)
"""
from threading import Thread
from random import randint


list_of_numbers = []


def preparing_list():
    """Fills the list with random numbers (10_000 elements)"""
    for i in range(10000):
        i = randint(1, 100)
        list_of_numbers.append(i)

    print(list_of_numbers)
    return list_of_numbers


def amount_calculation():
    """Finds the sum of the elements in a list"""
    amount = sum(list_of_numbers)
    print(f"Сума елементів у списку складає {amount}")
    return amount


def mean_calculation():
    """Finds the arithmetic mean of the elements in the list"""
    mean = sum(list_of_numbers)/len(list_of_numbers)
    print(f"\nСереднє арифметичне значення становить {mean}")
    return mean


t1 = Thread(target=preparing_list)
t2 = Thread(target=amount_calculation)
t3 = Thread(target=mean_calculation)

t1.start()
t1.join()
t2.start()
t3.start()
