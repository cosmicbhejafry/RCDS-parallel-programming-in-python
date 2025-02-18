from multiprocessing import Pool, current_process
import time
import math

import argparse

def sine_term(x,k):
    # multiprocessing.current_process().name is a way to get the name of the process
    exp_val = 2*k+1
    term_val = (x ** exp_val)/math.factorial(exp_val)

    if k%2==0:
        return term_val     
    else:
        return term_val*-1

def sine_approx_pool(x_val,num_taylor_terms,num_proc=2):    
    start_time = time.time()

    data = [(x_val,v) for v in list(range(num_taylor_terms))]

    with Pool(num_proc) as p:
        output = p.starmap(sine_term, data)

    end_time = time.time()

    # Print the output
    print(f'sin({x_val}) approximately equals {sum(output)} using the first {num_taylor_terms} terms')
    print(f'time taken {end_time-start_time}')
    return sum(output)

if __name__ == '__main__':

    parser=argparse.ArgumentParser(description="")
    parser.add_argument("--num_taylor_terms", nargs='?', type=int, default=10)
    parser.add_argument("--x", nargs='?', type=float, default=0.5)

    args=parser.parse_args()

    num_taylor_terms = args.num_taylor_terms
    x_val = args.x
    num_proc = 2
    
    sine_approx_pool(x_val,num_taylor_terms)
