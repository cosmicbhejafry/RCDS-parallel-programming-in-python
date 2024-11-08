import multiprocessing
import ctypes

# Create a shared memory array
# It is an array of 5 floats with an initial value of 0
a = multiprocessing.Array(ctypes.c_double, (0, 0, 0, 0, 0))