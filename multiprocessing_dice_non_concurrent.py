import random
import time

start_time = time.time()

n = int(1e9)

local_results = [0, 0, 0, 0, 0, 0]    

# Roll the dice n times
for i in range(n):
    current_roll = random.randint(1, 6)
    local_results [current_roll - 1] += 1

print(f'Time taken: {time.time() - start_time} seconds')