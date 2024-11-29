from scipy.stats import norm

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
print(simulate_share_price(100, 0.001, 0.02, 200))