import matplotlib.pyplot as plt
import random
import time
import sys

sys.setrecursionlimit(5000)

# merge method to unify two arrays into one
#
# l and ar are sorted arrays
def merge(l, r):

    # Gets the length of the given arrays
    nl = len(l); nr = len(r)

    # indexes to iterate over the arrays
    i = j = 0

    # final array
    a = []

    while i < nl and j < nr:

        if l[i] <= r[j]:
            a.append(l[i])
            i = i + 1
        else:
            a.append(r[j])
            j = j + 1
    
    while i < nl:
        a.append(l[i])
        i = i + 1

    while j < nr:
        a.append(r[j])
        j = j + 1

    return a
    
    
def mergeSort(a):

    if len(a) == 1:
        return a
    else:
        return merge(mergeSort(a[0:len(a)//2]), mergeSort(a[len(a)//2:len(a)]))

cases = [2, 5, 10, 20, 25, 50, 75, 100, 200, 250, 500, 750, 1000, 1250, 1500, 2000, 3000, 5000, 7500, 10000]

results = []

for case in range(0, len(cases)):

    arr = []

    for i in range(0, cases[case]):

        arr.append(random.randrange(500))
    

    now = time.monotonic()
    mergeSort(arr)
    end = time.monotonic()

    results.append(end-now)

plt.plot(cases, results)
plt.axis([0, 10000, 0, 0.02])
plt.title('Merge Sort')
plt.ylabel('time (seconds)')
plt.xlabel('n')
plt.show()
