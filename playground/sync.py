import requests
import time
from main import sites

# download pages synchronously


def download_url(url: str, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all(sites):
    with requests.Session() as session:
        for url in sites:
            download_url(url, session)


# Downloaded 160 in 10.46486520767212 seconds

if __name__ == "__main__":
    st = time.time()
    download_all(sites)
    et = time.time()
    duration = (et - st)
    print(f"Downloaded {len(sites)} in {duration} seconds")
