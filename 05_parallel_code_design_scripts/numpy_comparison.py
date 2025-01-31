import numpy as np
import time
from multiprocessing import Pool, current_process

if current_process().name == 'MainProcess':
    # Create the arrays
    n_values = int(1e5)
    array1 = np.random.rand(n_values)
    array2 = np.random.rand(n_values)

    # Perform the calculation with NumPy
    start_time = time.time()

    result = np.dot(array1, array2)

    print(f'Time taken with NumPy: {time.time() - start_time} seconds')

# Perform the calculation with multiprocessing
if __name__ == '__main__':
    start_time = time.time()

    n_processes = 2
    # Split the arrays into n_processes chunks
    array1_split = np.array_split(array1, n_processes)
    array2_split = np.array_split(array2, n_processes)

    # Create a Pool object with n_processes processes
    with Pool(n_processes) as p:
        # Apply the dot product to each pair of chunks
        result = sum(p.starmap(np.dot, zip(array1_split, array2_split)))

    print(f'Time taken with multiprocessing: {time.time() - start_time} seconds')


