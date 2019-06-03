import matplotlib.pyplot as plt
import random
import time
import sys

# increase the stack depth limit to allow deep recursions
sys.setrecursionlimit(5000)

# Insert Sort algorithm
# complexity: O(n^2)
#
# list: array to be sorted
def insertSort(list):

    # it begins to iterate from 1 to len(list) because
    # this algorithm has an inductive approach
    for index in range(1, len(list)):

        # gets the current value in the index position
        value = list[index]
        i = index - 1

        while i >= 0:

            # if the previous element is lesser than value
            # then an exchange must be made
            if value < list[i]:
                list[i+1] = list[i]
                list[i] = value
                i = i - 1
            
            # if not, it moves on to next case
            else:
                break
    
    # return the list ordered
    return list

# testcases
cases = [2, 5, 10, 20, 25, 50, 75, 100, 200, 250, 500, 750, 1000, 1250, 1500, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

# it stores the execution time for each testcase
results = []

# evaluates the testcases
for case in range(0, len(cases)):

    # array of elements depening on testcase
    arr = []

    # generates random elements in the array
    for i in range(0, cases[case]):
        arr.append(random.randrange(500))    

    # calls mergeSort()
    now = time.monotonic()
    insertSort(arr)
    end = time.monotonic()

    # stores the execution time of the call
    results.append(end-now)

# plot the results to be analized
plt.plot(cases, results)
plt.axis([0, 10000, 0, 2.5])
plt.title('Insert Sort')
plt.ylabel('time (seconds)')
plt.xlabel('n')
plt.show()