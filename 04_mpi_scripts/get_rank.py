# Run this script with the terminal command `mpiexec -n 4 python get_rank.py`

import mpi4py.MPI as MPI

# Get a reference to the current MPI.COMM_WORLD communicator
comm = MPI.COMM_WORLD

# Get the rank of the current process
rank = comm.Get_rank()

# Print the rank of the current process
print(f'This script is being run by Rank {rank}')