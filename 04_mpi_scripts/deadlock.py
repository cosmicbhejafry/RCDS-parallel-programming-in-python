# Run this script with the terminal command `mpiexec -n 2 python deadlock.py`

from mpi4py import MPI # type: ignore

# Get the communicator and the rank of the process
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# changing the order of the send resolves the deadlock
if rank == 0:
    # Receive the message from rank 1
    data = comm.recv(source=1)
    # Send a message to rank 1
    comm.send("Hello from rank 0", dest=1)
elif rank == 1:
    # Receive the message from rank 0
    data = comm.recv(source=0)
    # Send a message to rank 0
    comm.send("Hello from rank 1", dest=0)
    

# This print statement will never be reached as the program will deadlock
# You can force the code to stop Ctrl + C in the terminal
print(rank, data)