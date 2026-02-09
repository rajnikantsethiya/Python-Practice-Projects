import asyncio
import time
async def work():
    print("started working...")
    await asyncio.sleep(2) # when ran with this, it executed all 3 together
    # time.sleep(2) # when ran with this, it executed one by one due to blocking nature.
    print("Finished working !")

async def main():
    await asyncio.gather(work(), work(), work())
asyncio.run(main())