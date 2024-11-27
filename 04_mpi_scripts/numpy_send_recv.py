# Run this script with the terminal command `mpiexec -n 2 python numpy_send_recv.py`

from mpi4py import MPI
import numpy as np

# Get the communicator and the rank of the process
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    # If we're in rank 0, create an array of ten integers to send
    data = np.arange(10, dtype='f')
    # Send the array to rank 1
    comm.Send(data, dest=1)
elif rank == 1:
    # If we're in rank 1, create an array to receive the data
    data = np.empty(10, dtype='f')
    # data will initially contain junk values
    print('data before: ', data)
    # Receive the data from rank 0
    comm.Recv(data, source=0)
    print(rank, data)