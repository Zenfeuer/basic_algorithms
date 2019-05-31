import matplotlib.pyplot as plt
import random
import time
import sys

sys.setrecursionlimit(5000)

def merge(l, r):
    nl = len(l); nr = len(r)
    i = j = 0
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


def insertSort(list):
    for index in range(1, len(list)):
        value = list[index]
        i = index -1

        while i >= 0:
            if value < list[i]:
                list[i+1] = list[i]
                list[i] = value
                i = i - 1
            else:
                break
    
    return list


cases = [2, 5, 10, 20, 25, 50, 75, 100, 200, 250, 500, 750, 1000, 1250, 1500, 2000, 3000, 5000, 7500, 10000]

resultsMerge = []
resultsInsert = []

for case in range(0, len(cases)):

    arr = []

    for i in range(0, cases[case]):

        arr.append(random.randrange(500))
    

    now = time.monotonic()
    mergeSort(arr)
    end = time.monotonic()
    resultsMerge.append(end-now)

    now = time.monotonic()
    insertSort(arr)
    end = time.monotonic()
    resultsInsert.append(end-now)

plt.plot(cases, resultsMerge, 'r', cases, resultsInsert, 'g')
plt.axis([0, 10000, 0, 2.5])
plt.title('Time Analysis')
plt.ylabel('time (seconds)')
plt.xlabel('n')
plt.text(7900, 2.3, 'insertSort()', style='italic', color='green')
plt.text(8100, 0.1, 'mergeSort()', style='italic', color='red')
plt.show()
