import matplotlib.pyplot as plt
import random
import time
import sys

sys.setrecursionlimit(5000)

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
    arr = mergeSort(arr)
    binSearch(arr, item)
    end = time.monotonic()
    resultsIterative.append(end-now)

    now = time.monotonic()
    arr = mergeSort(arr)
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
plt.axis([0, 10000, 0, 2.5e-4])
plt.title('Time Analysis')
plt.ylabel('time (seconds)')
plt.xlabel('n')
plt.text(8300, 1.4e-4, 'recursive', style='italic', color='green')
plt.text(7800, 2e-4, 'iterative', style='italic', color='red')
plt.show()
