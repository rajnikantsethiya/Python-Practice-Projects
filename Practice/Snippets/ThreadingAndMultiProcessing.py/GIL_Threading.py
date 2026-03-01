import threading
import time

def Paint():
    print("started the count process")
    for i in range(100_999_000):
        count = 0
        count += 1
    print("Ended the count process")

T1 = threading.Thread(target=Paint, name="first")
T2 = threading.Thread(target=Paint, name="second")
start  = time.time()
T1.start()
T2.start()
T1.join()
T2.join()
end = time.time()

print(f"Finished countingg in {end - start:.2f} secs!")
