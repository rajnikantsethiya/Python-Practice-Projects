import asyncio
import threading
import time

async def main():
    print("started async..")
    await asyncio.sleep(2) # Non  blocking I/o
    print("Finished !")

def sub():
    print("started sub...")
    time.sleep(2) # Blocking I/o
    print("Finished !")

# Running blocking io
threading.Thread(target=sub, name="blockingIo").start()
# Running non blocking io
asyncio.run(main())

# Both works fine without delay or internal error.

