import asyncio
from random import randint


async def some_list(num):
    """Forms a list of numbers from 1 to the specified number inclusive."""
    list_of_numbers = []
    for j in range(1, num+1):
        list_of_numbers.append(j)
        await asyncio.sleep(0)
    print(f"The list for number {num} is: {list_of_numbers}")
    return list_of_numbers


async def client1():
    number1 = randint(1, 100)
    print(f"Client 1 {number1}")
    await some_list(number1)


async def client2():
    number2 = randint(1, 100)
    print(f"Client 2 {number2}")
    await some_list(number2)


async def client3():
    number3 = randint(1, 100)
    print(f"Client 3 {number3}")
    await some_list(number3)


async def manager():
    """Asynchronous execution of functions."""
    i = await asyncio.gather(client1(), client2(), client3())
    print(f"\nTotal result is {len(i)}")


if __name__ == "__main__":
    asyncio.run(manager())
