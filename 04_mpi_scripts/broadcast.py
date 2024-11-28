# Run this script with the terminal command `mpiexec -n 4 python broadcast.py`

import mpi4py.MPI as MPI

# Get the communicator and the rank of the process
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    # If the rank is 0, set the data to be broadcasted
    data = ['apples', 'bananas', 'cherries', 'dates']
else:
    # If the rank is not 0, we still need the variable to exist
    # Set it to None for now
    data = None

# Broadcast the data from rank 0 to all other ranks
data = comm.bcast(data, root=0)

# Each rank now has a copy of the data
print(f'Rank {rank} has data: {data}')