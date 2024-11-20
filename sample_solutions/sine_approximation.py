from multiprocessing import Process, Pool
from math import factorial, pi, sin

def sine_term(inputs):
    # This function calculates the nth term of the Taylor series expansion of sine(x)
    # The inputs are a list (x, n) where x is the value at which to evaluate the sine function

    # Extract x and n from the inputs list
    x = inputs[0]
    n = inputs[1]
    # Calculate and return the term
    return ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)

def sine_approx(x, n_terms):
    # This function calculates an approximation of the sine function at x using n_terms terms of the Taylor series expansion

    # Create a list of inputs for the sine_term function
    inputs = [[x, n] for n in range(n_terms)]
    print(inputs)

    # Create a pool of two threads to calculate the terms in parallel
    with Pool(2) as p:
        # Calculate the terms in parallel and store the results in a list
        terms = p.map(sine_term, inputs)

    # Return the sum of the terms
    return sum(terms)

if __name__ == '__main__':
    # Test the sine_approx function
    x = 0.5
    n_terms = 3
    print(sine_approx(x, n_terms), sin(x))

    x = pi
    n_terms = 5
    print(sine_approx(x, n_terms), sin(x))