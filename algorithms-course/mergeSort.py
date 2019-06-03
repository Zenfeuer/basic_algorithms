import matplotlib.pyplot as plt
import random
import time
import sys

# increase the stack depth limit to allow deep recursions
sys.setrecursionlimit(5000)

# merge method to unify two arrays into one
#
# l and r are sorted arrays
def merge(l, r):

    # Gets the length of the given arrays
    nl = len(l); nr = len(r)

    # indexes to iterate over the arrays
    i = j = 0

    # final array
    a = []

    while i < nl and j < nr:

        # if the i-th element in l is lesser or equals to the
        # j-th element in r, that means that elements in l are
        # still minor than the ones in r
        if l[i] <= r[j]:
            a.append(l[i])
            i = i + 1

        # if not, then the elements in r must be filled the
        # final array to be returned
        else:
            a.append(r[j])
            j = j + 1
    
    # fill with the remaining elements of l
    while i < nl:
        a.append(l[i])
        i = i + 1

    # fill with the remaining elements of r
    while j < nr:
        a.append(r[j])
        j = j + 1

    return a
    
# recursive algorithm to apply merge sort approach
# complexity: O(nlog(n))
def mergeSort(a):

    # base case
    if len(a) == 1:
        return a
    else:
        # this split the array into two arrays until the base case
        # it is reached. after, the arrays are merged with the
        # merge() method
        return merge(mergeSort(a[0:len(a)//2]), mergeSort(a[len(a)//2:len(a)]))

# testcases
cases = [2, 5, 10, 20, 25, 50, 75, 100, 200, 250, 500, 750, 1000, 1250, 1500, 2000, 3000, 5000, 7500, 10000]

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
    mergeSort(arr)
    end = time.monotonic()

    # stores the execution time of the call
    results.append(end-now)

# plot the results to be analized
plt.plot(cases, results)
plt.axis([0, 10000, 0, 0.02])
plt.title('Merge Sort')
plt.ylabel('time (seconds)')
plt.xlabel('n')
plt.show()
