#==============================================================================
# Work out the first ten digits of the sum of the following one-hundred
#  50-digit numbers.
#==============================================================================
import numpy as np
with open("problem13.txt", "r") as f:
    data = [int(line.strip()) for line in f]
    dataarray = np.array(data)

print(np.sum(data))