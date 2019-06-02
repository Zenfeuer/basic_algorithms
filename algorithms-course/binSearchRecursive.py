def binSearchRecursive(list, item, first, last):

    middle = (first + last)//2

    if list[middle] == item:
        return True, middle
    elif first > last:
        return False, -1
    else:
        if item < list[middle]:
            return binSearchRecursive(list, item, first, middle-1)
        else:
            return binSearchRecursive(list, item, middle+1, last)

# Testcases
print(binSearchRecursive([1, 4, 6, 9, 11, 17, 89, 91, 105], 17, 0, 9))
print(binSearchRecursive([1, 4, 6, 9, 11, 17, 89, 91, 105], 1, 0, 9))
print(binSearchRecursive([1, 4, 6, 9, 11, 17, 89, 91, 105], 88, 0, 9))