def bubbleSort(list):

    n = len(list)

    for i in range(1, n):
        for j in range(0, n - i):
            if list[j] > list[j+1]:
                tmp = list[j]
                list[j] = list[j+1]
                list[j+1] = tmp
    
    print(list)

# Testcases
bubbleSort([3, 5, 1, 9, 2, 67, 11, 6, 99, 12])
bubbleSort([99, 1])
bubbleSort([1, 2, 3, 4, 5, 6, 7, 8, 9])
bubbleSort([2, 2, 2, 2, 2, 1, 1, 1, 1, 1])
