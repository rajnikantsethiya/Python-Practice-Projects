import threading
import time

def Counting(wait):
    print("Started counting..")
    time.sleep(wait)
    print("Completed counting.")

start = time.time()
t1 = threading.Thread(target=Counting, args=(2,), name="counting1")
t2 = threading.Thread(target=Counting, args=(3,), name="counting2")

t1.start()
t2.start()
t1.join()
t2.join()

end = time.time()

print(f"Finished execution in {end - start:.2f} secs")