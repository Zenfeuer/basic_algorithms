# Binary Search Algorithm

# list: array of numbers (ordered)
# item: element to be found
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

# Testcases
print(binSearch([1, 4, 6, 9, 11, 17, 89, 91, 105], 17))
print(binSearch([1, 4, 6, 9, 11, 17, 89, 91, 105], 1))
print(binSearch([1, 4, 6, 9, 11, 17, 89, 91, 105], 88))

