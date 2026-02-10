import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        print(f"Received response with status code:{response.status}")

urls = ["http://httpbin.org/delay/2"] * 3

async def main():
    # aiohttp created a session and within that it fetches all the http requests
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        await asyncio.gather(*tasks)

asyncio.run(main())