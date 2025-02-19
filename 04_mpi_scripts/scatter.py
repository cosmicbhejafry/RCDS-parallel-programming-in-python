# Run this script with the terminal command `mpiexec -n 4 python scatter.py`

import mpi4py.MPI as MPI

# Get the communicator and the rank of the process
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
n_rank = comm.Get_size()

if rank == 0:
    # If the rank is 0, set the data to be scattered
    data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Divide the data into equal parts
    n_per_rank = len(data) / n_rank
    data_local = []
    for i in range(n_rank):
        data_local.append(data[int(i*n_per_rank):int((i+1)*n_per_rank)])

    # unequal data_local example
    # data_local = [[0,1],[2,3,4,5,6,7]]

    print(f'Rank 0 has prepared the data in data_local before sending: {data_local}')
    
else:
    # If the rank is not 0, we still need the variable to exist
    # Set it to None for now
    data_local = None

# Scatter the data from rank 0 to all other ranks
data_local = comm.scatter(data_local, root=0)

# Each rank now has a piece of the data in data_local
print(f'Rank {rank} has data: {data_local}')