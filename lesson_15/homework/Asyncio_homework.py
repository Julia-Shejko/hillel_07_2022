import asyncio


numbers = [10000, 2, 15, 1000000]


async def get_primes_amount(num: int) -> int:
    result = 0

    for i in range(2, num+1):
        counter = 0
        for j in range(1, i):
            if i % j == 0:
                counter += 1
        if counter == 1:
            result += 1

        await asyncio.sleep(0)

    print(result)
    return result


async def manager():
    tasks = [get_primes_amount(number) for number in numbers]
    await asyncio.gather(*tasks)


if __name__ == "__main__":

    for a in numbers:
        print(a)

    asyncio.run(manager())
