import math
import numpy as np

def get_permutation(lst, n):
    '''
    Gets the nth permutation of a list

    Parameters: 
    lst (list): A list
    n (int): The index of the permutation

    Returns:
    list: The nth permutation of the list
    '''

    # Create a local copy of the list
    lst = lst.copy()

    # Create a list of factorials
    factorials = [math.factorial(i) for i in range(0, len(lst))]
    factorials.reverse()

    # Create a list to store the permutation
    permutation = []

    # Loop through the factorials
    for i in factorials:
        # Get the index of the number to add
        index = n // i

        # Add the number to the permutation
        permutation.append(lst[index])

        # Remove the number from the list
        lst.pop(index)

        # Update n
        n = n % i

    return permutation

def get_city_distances(filepath='data/city_distances.csv'):
    '''
    Returns a list of distances between cities from a csv file

    Parameters:
    filepath (str): The path to the csv file

    Returns:
    list: The names of cities
    numpy.ndarray: The distances between cities
    '''

    # Read the csv file
    full_data = np.genfromtxt(filepath, delimiter=',', dtype='str')

    # Get the city names
    city_names = full_data[0, 1:]

    # Get the distances between cities
    distances = full_data[1:, 1:].astype(float)

    return city_names, distances


def get_total_route_length(route, distances):
    '''
    Returns the total length of a route

    Parameters:
    route (list): A list of city indices
    distances (numpy.ndarray): A 2D array of distances between cities

    Returns:
    float: The total length of the route
    '''

    # Create a variable to store the total length
    total_length = 0

    # Loop through the route
    for i in range(len(route) - 1):
        # Get the distance between the cities
        total_length += distances[route[i], route[i + 1]]

    # Add the distance from the last city to the first city
    total_length += distances[route[-1], route[0]]

    return total_length

city_names, distances = get_city_distances()







