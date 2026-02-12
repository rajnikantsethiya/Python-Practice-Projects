import asyncio
from concurrent.futures import ThreadPoolExecutor
import time 
def paint(color):
    time.sleep(2)
    print("Started painting...")
    return f"Painting ready with {color} color"

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        res = await loop.run_in_executor(pool, paint, "Red")
        print(res)

asyncio.run(main())

# This program shows how to run the blocking task without stopping the entire python event loop or main thread.
# How this works -> Main event loop running -> 
# ThreadPoolExecutor creates a new pool or threads to run the blocking code. -> 
# run_in_executor bridges back the pool to the main event loop once completed as it uses await
