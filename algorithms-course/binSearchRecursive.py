#Homework: Binary Search Algorithm (Recursive Approach)
#
# list: array of numbers (ordered)
# item: element to be found
# first: inferior bound
# last: superior bound
#
# returns found, positionFound
# found: if item exists in the array
# positionFound: item's position, -1 if not found
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

# Testcases
print(binSearchRecursive([1, 4, 6, 9, 11, 17, 89, 91, 105], 17, 0, 9))
print(binSearchRecursive([1, 4, 6, 9, 11, 17, 89, 91, 105], 1, 0, 9))
print(binSearchRecursive([1, 4, 6, 9, 11, 17, 89, 91, 105], 88, 0, 9))