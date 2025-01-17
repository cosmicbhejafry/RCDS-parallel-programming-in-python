# Run this script with the command: mpiexec -n 4 python exploding_dice.py

import random
import mpi4py.MPI as MPI
import numpy as np

def roll_die():
    result = random.randint(1, 6)

    if result == 6:
        return result  + roll_die()
    else:
        return result
    
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
n_rank = comm.Get_size()

n_rolls = int(1e8)

n_rolls_this_rank = n_rolls // n_rank + (n_rolls % n_rank > rank)

local_rolls = np.fromiter((roll_die() for _ in range(n_rolls_this_rank)), int)

local_total = sum(local_rolls)

local_square_total = np.dot(local_rolls, local_rolls)

local_over_20 = np.sum(local_rolls > 20)

global_total = comm.reduce(local_total, op=MPI.SUM, root=0)
global_square_total = comm.reduce(local_square_total, op=MPI.SUM, root=0)
global_over_20 = comm.reduce(local_over_20, op=MPI.SUM, root=0)

if rank == 0:
    mean = global_total / n_rolls
    std = np.sqrt(global_square_total / n_rolls - mean**2)
    p_over_20 = global_over_20 / n_rolls

    print(f'The mean of the rolls is {mean}')
    print(f'The standard deviation of the rolls is {std}')
    print(f'The probability of rolling over 20 is {p_over_20}')

