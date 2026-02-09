import asyncio

async def main():
    print("Start paiting...")
    await asyncio.sleep(2) # If not awaited, error thrown -> coroutine never awaited
    print("Finished !")
# to run the asyncio, if main is not provided, error thrown -> coroutine expected
asyncio.run(main())