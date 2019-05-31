import matplotlib.pyplot as plt
import random
import time
import sys

sys.setrecursionlimit(5000)

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

cases = [2, 5, 10, 20, 25, 50, 75, 100, 200, 250, 500, 750, 1000, 1250, 1500, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

results = []

for case in range(0, len(cases)):

    arr = []

    for i in range(0, cases[case]):

        arr.append(random.randrange(500))
    

    now = time.monotonic()
    insertSort(arr)
    end = time.monotonic()

    results.append(end-now)


print(results)

plt.plot(cases, results)
plt.ylabel('time (seconds)')
plt.xlabel('n')
plt.show()