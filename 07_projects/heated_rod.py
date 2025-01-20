import numpy as np
import matplotlib.pyplot as plt

def get_peak_temeprature(boundary_temeprature, heating_rate, rod_length, diffusion_coefficient, n_points=100):
    '''
    Find the peak staedy state temperature in a rod heated at a constant rate.
    
    Parameters

    boundary_temperature (float): The temperature of the rod at the left and right boundaries (K).
    heating_rate (float): The rate at which the rod is heated (K/s).
    rod_length (float): The length of the rod (m).
    diffusion_coefficient (float): The diffusion coefficient of the rod (m^2s^-1).
    n_points (int): The number of points to use in the numerical solution.
    '''

    dx = rod_length / (n_points - 1)

    # Create the heat diffusion matrix
    diffusion_matrix = np.zeros((n_points, n_points))
    np.fill_diagonal(diffusion_matrix, -2 * diffusion_coefficient / dx ** 2)
    np.fill_diagonal(diffusion_matrix[1:], diffusion_coefficient / dx ** 2)
    np.fill_diagonal(diffusion_matrix[:, 1:], diffusion_coefficient / dx ** 2)

    # Set the boundary conditions
    diffusion_matrix[0, 0] = 1
    diffusion_matrix[0, 1] = 0
    diffusion_matrix[-1, -1] = 1
    diffusion_matrix[-1, -2] = 0

    rhs = np.full(n_points, -heating_rate)
    rhs[0] = boundary_temeprature
    rhs[-1] = boundary_temeprature

    # Solve the system of equations
    temperature = np.linalg.solve(diffusion_matrix, rhs)

    # Find and return the peak temperature
    peak_temperature = np.max(temperature)

    return peak_temperature

def plot_histogram(data):
    '''
    Make a histogram of the data and save it to a file.
    
    Parameters
    
    data (array_like): A list of data to plot. Could be a list, Numpy array, etc
    
    Returns
    
    None
    '''
    plt.hist(data, bins=20, density = True)
    plt.xlabel('Peak Temperature')
    plt.ylabel('Probability Density')
    plt.title('Histogram of Peak Temperature')
    plt.savefig('outputs/peak_temperature_histogram.png')

# An example call to the function
# This uses the same values as the problem description, with a thermal diffusivity of 1
print(get_peak_temeprature(300, 10, 10, 1))