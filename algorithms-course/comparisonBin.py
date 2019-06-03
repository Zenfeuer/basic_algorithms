import matplotlib.pyplot as plt
import random
import time
import sys

sys.setrecursionlimit(5000)

def binSearch(list, item):

    # inferior bound
    first = 0

    # superior bound
    last = len(list) - 1

    # boolean to tell if item was found
    found = False

    # position where the desired item is located, -1 by default, this means that
    # the item does not exist in the list
    positionFound = -1

    # first and last are the boundaries of the search scope on each iteration
    # those boundaries are going to be changed on each iteration
    while first <= last and not found:

        # it calculates the middle position in the array depending on the 
        # current  values of first and last
        middle = (first + last)//2

        # it verifies if item is located in middle position
        if list[middle] == item:

            # if it is found, it marks found as True
            found = True

            # it saves the item's position
            positionFound = middle
        else:

            # if it is not found, it must update the current bound values

            # if the desired item is lesser than the current item in middle
            # position, then it must move the superior bound to just before
            # middle value. 
            if item < list[middle]:
                last = middle - 1

            # if the desired item is greater than the current item in middle
            # position, then it must move the inferior bound to just after 
            # middle value.
            else:
                first = middle + 1
    
    # return if item is found and the position where it is located
    return found, positionFound

def binSearchRecursive(list, item, first, last):

    # it calculates the middle position in the array depending on the 
    # current  values of first and last
    middle = (first + last)//2

    # base case: first and last are the boundaries of the search 
    # scope on each recursion level. If first surpass last index,
    # then the item does not exist in the list.
    if first > last:

        # returns not found
        return False, -1

    # base case: it verifies if item is located in middle position
    elif list[middle] == item:

        # if it is found, returns that it is found and the position
        return True, middle

    else:
        # if it is not found, it must update the current bound values

        # if the desired item is lesser than the current item in middle
        # position, then it must move the superior bound to just before
        # middle value.
        if item < list[middle]:
            return binSearchRecursive(list, item, first, middle-1)
        
        # if the desired item is greater than the current item in middle
        # position, then it must move the inferior bound to just after 
        # middle value.
        else:
            return binSearchRecursive(list, item, middle+1, last)

cases = [2, 5, 10, 20, 25, 50, 75, 100, 200, 250, 500, 750, 1000, 1250, 1500, 2000, 3000, 5000, 7500, 10000]

resultsIterative = []
resultsRecursive = []

for case in range(0, len(cases)):

    arr = []

    for i in range(0, cases[case]):

        arr.append(random.randrange(500))
    
    item = 10000

    now = time.monotonic()
    binSearch(arr, item)
    end = time.monotonic()
    resultsIterative.append(end-now)

    now = time.monotonic()
    binSearchRecursive(arr, item, 0, len(arr)-1)
    end = time.monotonic()
    resultsRecursive.append(end-now)

for k in range(0, 100):
    for case in range(0, len(cases)):

        arr = []

        for i in range(0, cases[case]):

            arr.append(random.randrange(500))
        
        item = 10000

        now = time.monotonic()
        binSearch(arr, item)
        end = time.monotonic()
        resultsIterative[case] += (end-now)

        now = time.monotonic()
        binSearchRecursive(arr, item, 0, len(arr)-1)
        end = time.monotonic()
        resultsRecursive[case] += (end-now)

for k in range(0, len(cases)):
    resultsIterative[k] = resultsIterative[k]/100
    resultsRecursive[k] = resultsRecursive[k]/100


plt.plot(cases, resultsIterative, 'r', cases, resultsRecursive, 'g')
plt.axis([0, 10000, 0, 6e-6])
plt.title('Time Analysis')
plt.ylabel('time (seconds)')
plt.xlabel('n')
plt.text(7900, 5e-6, 'iterative', style='italic', color='green')
plt.text(8100, 5.5e-6, 'recursive', style='italic', color='red')
plt.show()
