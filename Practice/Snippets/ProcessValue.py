from multiprocessing import Process, Value

def Play(players):
    for _ in range(100000):
        # mannual lock for value in memory
        with players.get_lock():
            players.value += 1


if __name__ == "__main__":
    players = Value('i', 0)
    processes = [Process(target=Play, args=(players, )) for _ in range(4)]
    [p.start() for p in processes]
    [p.join() for p in processes]

    # Dry run
    # created 4 process
    # each process will increase number from 0 to 100000
    # in Join all 4 will combine - (0 -> 100000) * 4 = 400000
    print("final counter value:", players.value) # 400000



