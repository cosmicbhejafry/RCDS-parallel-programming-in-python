# We can say that the price of a share on a given day is equal to the price of the share on the previous day multiplied by a random number drawn from a normal distribution with a given mean and standard deviation. 
# We can simulate this process by generating a random number for each day and multiplying it by the share price on the previous day. 

# We can do this for a number of days to simulate the share price over time. 
# In the file [`share_price.py`](04_mpi_scripts/share_price.py) there is a function `simulate_share_price` which takes the initial share price, 
# the mean of the normal distribution, the standard deviation of the normal distribution, 
# and the number of days to simulate. 
# This function returns the share price at the end of the final day of the simulated period.

# Each call to this function will return a different final share price as a different set of random numbers will have been generated. 
# This means we can call the function multiple times to get a distribution of final share prices. 
# Your task is to write code which will call this code `n` times in total, 
# split across each rank in the communicator. 
# Once this is done, use collective communication to 
# collect the results on rank zero and print the mean, standard deviation, minimum and maximum values of the final share prices. 
# The code should be able to be run with any number of ranks. 
# Your code should have values for the initial share price, mean, standard deviation, and number of days to simulate, and the number of simulations to run hard-coded into the script. 
# Try the following values:

from scipy.stats import norm
from mpi4py import MPI
import numpy as np

def simulate_share_price(initial_price, daily_change_mean, daily_change_std, n_days):
    """
    Simulates the price of a share over a number of days.

    Parameters:
    initial_price (float): The initial price of the share.
    daily_change_mean (float): The average daily fractional change in the share price.
    daily_change_std (float): The standard deviation of the daily fractional change in the share price.
    n_days (int): The number of days to simulate.

    Returns:
    float: The simulated share price after n_days.
    """

    return initial_price * norm.rvs(loc=1 + daily_change_mean, scale=daily_change_std, size=n_days).prod()

# This is a sample call to the function that returns the result of one simulation.
# Feel free to delete it once you're happy with how the function works.
# print(simulate_share_price(100, 0.001, 0.02, 200))

# * Initial share price: 100
# * Mean fractional daily change: 0.001
# * Standard deviation of fractional daily change: 0.02
# * Number of days to simulate: 100
# * Number of simulations: 1000


# Get the communicator and the rank of the process
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Get the total number of ranks in the communicator
n_rank = comm.Get_size()

num_sims = 10000

init_price = 100
mean_change = 0.001
stdev_daily = 0.02
num_days_sim = 100

# distribute num_sims between each rank
num_sim_per_rank = num_sims // n_rank

if rank < num_sims % n_rank:
    # If the rank is less than the remainder, it will generate one more number
    # This is to ensure that the right number of numbers are generated
    num_sim_per_rank_loc = num_sim_per_rank+1
else:
    num_sim_per_rank_loc = num_sim_per_rank

## simulate runs for each rank
price_results_loc = []
for ix in range(num_sim_per_rank_loc):
    end_price = simulate_share_price(init_price,mean_change,stdev_daily,num_days_sim)
    price_results_loc.append(end_price)

# gather data
data = comm.gather(price_results_loc, root=0)


## alternate way using reduce:
# calculate the sum and sum of squares for each 'price_results_loc'

## THIS DOES IT ARRAY ELEMENT WISE
data_sum = comm.reduce(price_results_loc, op=MPI.SUM, root=0)

price_results_loc_sq = [v**2 for v in price_results_loc]
data_sum_sq = comm.reduce(price_results_loc_sq,op=MPI.SUM,root=0)
# for min and max use MPI.MIN
data_min = comm.reduce(np.min(price_results_loc),op=MPI.MIN,root=0)
data_max = comm.reduce(np.max(price_results_loc),op=MPI.MAX,root=0)

if rank==0:

    print(len(data_sum))

    data = np.array(sum(data, []))
    print('with gather:')
    print(f'mean : {np.mean(data)}')
    print(f'std : {np.std(data)}')
    print(f'min : {np.min(data)}')
    print(f'max : {np.max(data)}')

    print('with reduce:')
    meanv = sum(data_sum)/num_sims
    print(f'mean : {meanv}')
    stdev = ((sum(data_sum_sq)/num_sims)-(meanv**2))
    print(f'std : {np.sqrt(stdev)}')
    print(f'min : {np.min(data_min)}')
    print(f'max : {np.max(data_max)}')

    # print(f'median : {np.quantile(data,0.5)}') 