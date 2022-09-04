# NOTE: Get 100_000 rockets.
#       Run in 1000 threads
#       Each thread runs rockets asynchronously

import asyncio
from random import randint, random
from threading import Thread


def get_random_delay():
    """
    Just return random value from 0 to 2.
    Represent seconds of delay.
    """
    return random() * randint(1, 2)


def get_random_countdown():
    """Just return integer in range 3 <= N <= 5."""
    return randint(3, 5)


class AsyncRocket:
    """
    This class is responsible for running async rockets.
    Every rocket has its own delay and countdown.
    """

    def __init__(self, name) -> None:
        self.delay = get_random_delay()
        self.countdown = get_random_countdown()
        self.name = name

    async def _countdown(self):
        """Human-base countdown."""

        for i in range(self.countdown + 1, 0, -1):
            print(f"{i}...")
            await asyncio.sleep(1)

    async def _delay(self):
        print(f"🕐 Delay for {self.delay} seconds...")
        await asyncio.sleep(self.delay)

    async def run(self):
        # Do the countdown before start the rocket
        print(f"\nPrepare the {self.name} ✅")
        await self._countdown()

        # Check the delay
        await self._delay()

        # Show success message
        print(f"🚀 {self.name} go to the moon...")


async def run_async(rockets):
    tasks = [rocket.run() for rocket in rockets]
    await asyncio.gather(*tasks)


def run_super():
    async_rockets = list(AsyncRocket(name=f"Rocket {i}") for i in range(1, 100_001))
    async_rockets1 = [async_rockets[i:i + 100] for i in range(0, len(async_rockets), 100)]
    count = 0

    def hundred_async_run():
        asyncio.run(run_async(async_rockets1[count]))

    for i in range(1, 1001):

        thread = Thread(target=hundred_async_run)
        thread.start()
        count += 1


if __name__ == "__main__":

    run_super()
