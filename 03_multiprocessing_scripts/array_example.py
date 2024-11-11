import multiprocessing
import ctypes
import random

def roll_n_dice(n, array):
    for i in range(n):
        current_roll = random.randint(1, 6)
        with array.get_lock():
            array[current_roll - 1] += 1

if __name__ == '__main__':
    # Create a shared memory array
    # It is an array of 6 floats with an initial value of 0
    a = multiprocessing.Array(ctypes.c_int, (0, 0, 0, 0, 0, 0))

    n_rolls_total = int(1e6)

    # Create n_process processes
    n_process = 4
    processes = []
    for i in range(n_process):
        p = multiprocessing.Process(target=roll_n_dice, args=(n_rolls_total // n_process, a))
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()

    # Print the results
    print(f'Results after {n_rolls_total} rolls: {list(a[:])}')