# Run this script with the terminal command `mpiexec -n 4 python gather.py`

import mpi4py.MPI as MPI

# Get the communicator and the rank of the process
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
n_rank = comm.Get_size()

# We're aiming to write an array with square of each number.
# We'll compute part of the array on each rank and then gather the results.
n = 10
i_local_start = int(rank * n / n_rank)
i_local_stop = int((rank + 1) * n / n_rank)
data_local = [i**2 for i in range(i_local_start, i_local_stop)]

# Print the local data on each rank
print(f'Rank {rank} has data: {data_local}')

# Gather the data from all ranks to rank 0
data = comm.gather(data_local, root=0)

# Rank 0 now has all the data
if rank == 0:
    print(f'Rank {rank} has data: {data} before flattening')
    # Flatten the list of lists into a single list
    data = sum(data, [])
    print(f'Rank {rank} has data: {data} after flattening')