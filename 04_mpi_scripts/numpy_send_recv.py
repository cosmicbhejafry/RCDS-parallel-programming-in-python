# Run this script with the terminal command `mpiexec -n 2 python numpy_send_recv.py`

from mpi4py import MPI
import numpy as np

# Get the communicator and the rank of the process
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Get the total number of ranks in the communicator
n_rank = comm.Get_size()

if rank==0:
    # generate a random array of 100 floats with a minimum of zero and maximum of 10 using the function call `random_float_array(0, 10, 100)` on rank 0. 
    random_data = np.random.random(100)*(10-0)+0


    # Then send this array to all other ranks. 
    for i in range(1,n_rank):
        comm.Send(random_data,dest=i)


    # Each rank, including rank 0, should calculate the given value function

    # Each rank should then send the result back to rank 0. 

    # Rank 0 should assemble the results into a list `results` 
    # whose $i$ th element is the sum of the powers of the array elements calculated by rank $i$. 
    
    # Finally, rank 0 should print the list of results.

## TODO: FINISH EXERCISE