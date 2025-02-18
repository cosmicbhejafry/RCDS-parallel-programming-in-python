import numpy as np
from mpi4py import MPI

def random_float_array(minimum, maximum, size):
    '''Generates a random array of floats between minimum and maximum.

    Args:
        minimum (float): minimum value which may be in the array
        maximum (float): maximum value which may be in the array
        size (int): size of the array
        
    Returns:
        np.array: array of floats between minimum and maximum'''
    return np.random.random(size) * (maximum - minimum) + minimum

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

