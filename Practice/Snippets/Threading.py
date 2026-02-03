import threading
import time

def Sketch():
    print("Creating a sketch with pencils !")

def Paint():
    print("Painting with a dusky color !")

# creating thread
T1 = threading.Thread(target=Sketch)
T2 = threading.Thread(target=Paint)

start = time.time()
# starting threads and joining them to get all other gets completed
T1.start()
T2.start()
T1.join()
T2.join()
end = time.time()

print(f"Total time is {end - start}")
