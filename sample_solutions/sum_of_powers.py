import numpy as np
# Run this script with the terminal command `mpiexec -n 2 python sum_of_powers.py`
# You may replace the "2" in the command above to use a different number of ranks

from mpi4py import MPI
import numpy as np

def random_float_array(minimum, maximum, size):
    return np.random.random(size) * (maximum - minimum) + minimum

# Get the communicator and the rank of the process
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
n_rank = comm.Get_size()

# Number of data points
n_data = 100

if rank == 0:
    # If we're in rank 0, create an array of random floats to send    
    data = random_float_array(0, 10, n_data)

    # Send the result to each rank
    # We can use "Send" instead of "send" as it's a Numpy array
    for i in range(1, n_rank):
        comm.Send(data, dest=i)

    # The first entry in the results should be generated on this rank
    # It is the sum of the data
    # Convert it to a native Python float and place it in the results list
    results = [float(sum(data))]

    # Receive the results from the other ranks
    for i in range(1, n_rank):
        # Convert each result to a float and append it to the results list
        results.append(float(comm.recv(source=i)))

    print(results)

else:
    # If we're in another rank, create an array to receive the data
    data = np.empty(n_data, dtype=float)
    # Receive the data from rank 0
    comm.Recv(data, source=0)
    # Send the sum of the data raised to the appropriate power to rank 0
    comm.send(sum(data ** (rank + 1)), dest=0)

    

    

