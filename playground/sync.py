import requests
import time

# download pages synchronously


def download_url(url: str, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all(sites):
    with requests.Session() as session:
        for url in sites:
            download_url(url, session)


if __name__ == "__main__":
    sites = [
        "http://google.com",
        "http://olympus.realpython.org/dice",
        "https://www.jython.org",
    ]
    st = time.time()
    download_all(sites)
    et = time.time()
    duration = (et - st)
    print(f"Downloaded {len(sites)} in {duration} seconds")
