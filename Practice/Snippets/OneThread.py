import threading
import time

def Counting():
    print("Started counting..")
    time.sleep(2)
    print("Completed counting.")

def Distribute():
    print("Started distributing..")
    time.sleep(3)
    print("Completed distributing.")

start = time.time()
t1 = threading.Thread(target=Counting, name="counting")
t2 = threading.Thread(target=Distribute, name="distributing")
t1.start()
t2.start()
t1.join()
t2.join()

end = time.time()

print(f"Finished execution in {end - start:.2f} secs")