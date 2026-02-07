from multiprocessing import Process, Queue

def Play(q):
    # Adding in quene
    q.put("Let's play cricket !")

if __name__ == '__main__':
    # creating quene
    q = Queue()
    p1 = Process(target=Play, args=(q,))

    p1.start()
    p1.join()
    # extracting from quene
    print("Finished executing ", q.get())

