# Run this script with the terminal command `mpiexec -n 2 python send_recv.py`

from mpi4py import MPI # type: ignore

# Get the communicator and the rank of the process
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    # If we're in rank 0, send a dictionary to rank 1
    data = {'a': 7, 'b': 3.14}
    comm.send(data, dest=1)
    
elif rank == 1:
    # If we're in rank 1, receive the dictionary from rank 0
    data = comm.recv(source=0)
    print(rank, data)