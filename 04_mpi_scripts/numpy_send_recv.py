# Run this script with the terminal command `mpiexec -n 2 python numpy_send_recv.py`

from mpi4py import MPI
import numpy as np

# Get the communicator and the rank of the process
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Get the total number of ranks in the communicator
n_rank = comm.Get_size()


## TODO: FINISH EXERCISE