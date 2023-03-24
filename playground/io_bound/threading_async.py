import concurrent.futures
import threading
from main import sites
import time
import requests
import debugpy
debugpy.debug_this_thread()


# download pages async (threading) - pre-emptive multitasking

thread_local = threading.local()


def get_session():
    # shared requests session (create if not exist + get)
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_url(foo, url: str):
    session = get_session()
    print(f"foo : {foo} --- url : {url}")
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_url, sites)


# Downloaded 160 in 1.9363200664520264 seconds
if __name__ == "__main__":
    st = time.time()
    download_all(sites)
    et = time.time()
    duration = (et - st)
    print(f"Downloaded {len(sites)} in {duration} seconds")
