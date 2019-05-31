

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

print([3, 5, 1, 9, 2, 67, 11, 6, 99, 12])
print(insertSort([3, 5, 1, 9, 2, 67, 11, 6, 99, 12]))
print([99, 1])
print(insertSort([99, 1]))
print([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(insertSort([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print([2, 2, 2, 2, 2, 1, 1, 1, 1, 1])
print(insertSort([2, 2, 2, 2, 2, 1, 1, 1, 1, 1]))