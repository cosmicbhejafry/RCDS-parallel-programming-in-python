import numpy as np

def random_float_array(minimum, maximum, size):
    return np.random.random(size) * (maximum - minimum) + minimum
