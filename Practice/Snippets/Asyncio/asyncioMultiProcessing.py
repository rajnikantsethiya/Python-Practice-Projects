import asyncio
from concurrent.futures import ProcessPoolExecutor

def encryption(data):
    return f"Encrypted Data: {data[:: -1]} "

async def main():
    loop =  asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        res = await loop.run_in_executor(pool, encryption, "I am awesome")
        print(res)

if __name__ == '__main__':
    asyncio.run(main())