import aiohttp
import asyncio
import time
from main import sites


async def download_site(session, url):
    async with session.get(url) as res:
        print(f"Read {res.content_length} from {url}")


async def download_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        # run all tasks
        for url in urls:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        # gather results
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    st = time.time()
    asyncio.get_event_loop().run_until_complete(download_all(sites))
    et = time.time()
    duration = (et - st)
    print(f"Downloaded {len(sites)} in {duration} seconds")
