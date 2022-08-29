import asyncio
from random import randint


async def client1():
    number1 = randint(1, 1000000)
    print(f"Client 1 {number1}")
    await get_primes_amount(number1)


async def client2():
    number2 = randint(1, 1000000)
    print(f"Client 2 {number2}")
    await get_primes_amount(number2)


async def client3():
    number3 = randint(1, 1000000)
    print(f"Client 3 {number3}")
    await get_primes_amount(number3)


async def manager():
    i = await asyncio.gather(client1(), client2(), client3())
    print(f"\nTotal result is {len(i)}")


async def get_primes_amount(num):
    counter = 0
    for j in range(1, num+1):
        if num % j == 0:
            counter += 1
            print(f"✌️number {num}   in counter: ️{counter}")
        await asyncio.sleep(0)
        if counter > 2:
            break
    print(f"Number {num} has been processed {counter} times")

    return counter


if __name__ == "__main__":
    asyncio.run(manager())
