import matplotlib.pyplot as plt
import random
import time
import sys

# increase the stack depth limit to allow deep recursions
sys.setrecursionlimit(5000)

# Pascal Triangle's Algorithm
#
# Given n, k, it determines the binomial coefficient 
# in the Pascal Triangle
#
# returns the coefficient depending on given n, k
def pascal(n, k):

    # Base case
    if n == 0 or k == 0 or n == k:
        return 1
    
    # According to the recurrent expression, it calls 
    # recursively until it gets base case
    return pascal(n-1, k) + pascal(n-1, k-1)

# testcases
cases = [2, 5, 10, 20, 25, 50, 75, 100, 200, 250, 500, 750, 1000, 1250]

# it stores the execution time for each testcase
results = []

#  evaluates the testcases
for case in range(0, len(cases)):
    now = time.monotonic()
    pascal(cases[case], 3)
    end = time.monotonic()
    results.append(end-now)

# plots the graphics/chart to analize the results
plt.plot(cases, results, 'r')
plt.axis([0, 1250, 0, 75])
plt.title('Time Analysis')
plt.ylabel('time (seconds)')
plt.xlabel('n')
plt.show()