

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


#Testcases
print([3, 5, 1, 9, 2, 67, 11, 6, 99, 12])
print(mergeSort([3, 5, 1, 9, 2, 67, 11, 6, 99, 12]))
print([99, 1])
print(mergeSort([99, 1]))
print([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(mergeSort([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print([2, 2, 2, 2, 2, 1, 1, 1, 1, 1])
print(mergeSort([2, 2, 2, 2, 2, 1, 1, 1, 1, 1]))
