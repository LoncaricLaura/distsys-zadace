import asyncio
import numpy as np
import psutil
import time

async def afunc1():
    x = []
    for _ in range(10):
        time.sleep(0.9)
        x.append(np.random.normal(size=(1000000)))
    return x
        

async def afunc2():
    return psutil.cpu_percent(10)


async def main():
    await afunc1()
    cpu = await afunc2()
    print('The CPU usage is: ', cpu)


if __name__ == "__main__":
    asyncio.run(main())