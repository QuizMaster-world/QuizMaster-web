import asyncio
import time

async def my_func():
    start = time.time()
    sleep_func = asyncio.sleep(2)  # function called, but not awaited
    print(time.time() - start)
    await sleep_func  # actual await
    print(time.time() - start)

asyncio.run(my_func())
