from multiprocessing import Process
import time
def Paintings(i):
    print(f"started Painting the item #{i}")
    # time.sleep(3) # enable to see the tasks running in sync
    print(f"Finished Painting the item #{i}")
    
# This is to wait for initial process is bootstrapped and then start the below one
if __name__ == "__main__":
    # making use of list comprehension and passing tuple args
    processes = [
            Process(target=Paintings, args=(i+1,), name="Painting")
            for i in range(3)
        ]

    # starting the processes
    for P in processes:
        P.start()
    
    # joining the processes
    for P in processes:
        P.join()
    
    print("Finished Sketching and painting !")



