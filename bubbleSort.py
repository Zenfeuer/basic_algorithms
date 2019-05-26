# Homework: Bubble Sort Algorithm
# Complexity: O(n(n-1)/2) = O(n^2)

# list: array of numbers (unsorted)
# isAsc: desired order. True: ascending | False: descending
def bubbleSort(list, isAsc):

    # saves the length of the list
    n = len(list)

    # for each iteration, greatest/smallest element must be moved to n-i
    # position in the array, this ensures that the array it is ordered by the
    # specified order (ascending or descending)
    for i in range(1, n):

        # j-th and (j+1)-th element must be compared to evaluatr if they need to
        # be swapped according to the desired order
        for j in range(0, n - i):

            # isAsc and list[j] > list[j+1]:
            # if the desired order is ascending and the j-th element is greater
            # than the (j+1)-th element, then a swap must be made
            #
            # not isAsc and list[j] < list[j+1]:
            # if the desired order is descending and the j-th element is lesser
            # than the (j+1)-th element, then a swap must be made
            if (isAsc and list[j] > list[j+1]) or (not isAsc and list[j] < list[j+1]):

                # Swapping j-th and (j+1)-th elements
                tmp = list[j]
                list[j] = list[j+1]
                list[j+1] = tmp

    # returns the sorted list
    return list

# Testcases (ascending order)
print("---------- Ascending Order ----------")
print(bubbleSort([3, 5, 1, 9, 2, 67, 11, 6, 99, 12], True))
print(bubbleSort([99, 1], True))
print(bubbleSort([1, 2, 3, 4, 5, 6, 7, 8, 9], True))
print(bubbleSort([2, 2, 2, 2, 2, 1, 1, 1, 1, 1], True))
print("-------------------------------------")

# Testcases (descending order)
print("---------- Descending Order ----------")
print(bubbleSort([3, 5, 1, 9, 2, 67, 11, 6, 99, 12], False))
print(bubbleSort([99, 1], False))
print(bubbleSort([1, 2, 3, 4, 5, 6, 7, 8, 9], False))
print(bubbleSort([2, 2, 2, 2, 2, 1, 1, 1, 1, 1], False))
print("--------------------------------------")