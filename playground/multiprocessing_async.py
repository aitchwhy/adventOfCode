from main import sites

import requests
import multiprocessing
import time

session = None


def set_global_session():
    global session
    if not session:
        session = requests.Session()


def download_site(url):
    with session.get(url) as res:
        name = multiprocessing.current_process().name
        print(f"{name} : Read {len(res.content)} from {url}")


def download_all(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)


# Downloaded 160 in 2.6122677326202393 seconds
if __name__ == "__main__":
    st = time.time()
    download_all(sites)
    et = time.time()
    duration = (et - st)
    print(f"Downloaded {len(sites)} in {duration} seconds")
