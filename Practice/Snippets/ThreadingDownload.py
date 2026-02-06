import threading
import requests
def download(url):
    res = requests.get(url=url)
    print(f"Completed downloading from {url}, size: {len(res.content)}")

urls = [
    "https://httpbin.org/image/jpeg"
    "https://httpbin.org/image/png"
    "https://httpbin.org/image/svg"
    ]

threads = []
for url in urls:
    t = threading.Thread(target=download, args=(url, ))
    threads.append(t)

for i in threads:
    i.start()


for i in threads:
    i.join()

print("Finished downloading")