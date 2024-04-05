import asyncio
import time


async def greet(name, delay):
    await asyncio.sleep(delay)
    print(f'{name}: I waited {delay} milli-seconds before saying "hello"')


async def main():
    task_1 = asyncio.create_task(greet("t1", 180))
    task_2 = asyncio.create_task(greet("t2", 120))
    task_3 = asyncio.create_task(greet("t3", 120))

    start_time = time.time()

    print("0.00ms: Program Start")

    await task_1
    await task_2
    await task_3

    print(f"{time.time() - start_time:.2f}ms: Program End")


asyncio.run(main())
