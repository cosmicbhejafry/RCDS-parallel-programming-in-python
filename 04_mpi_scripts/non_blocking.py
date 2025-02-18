# Run this script using the command: mpiexec -n 2 python non_blocking.py

from mpi4py import MPI # type: ignore

# Get the communicator and the rank of the process
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    # Send the integer 100 to rank 1
    req = comm.isend(100,dest=1)
    # Wait for the request to complete
    req.wait()

elif rank == 1:
    # Receive the integer from rank 0
    req = comm.irecv(source=0)
    # Wait for the request to complete and get the data
    data = req.wait()
    print(data)