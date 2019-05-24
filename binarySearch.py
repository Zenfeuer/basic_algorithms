# Binary Search Algorithm

# list: array of numbers (ordered)
# item: element to be found
def binSearch(list, item):

    # inferior bound
    first = 0

    # superior bound
    last = len(list) - 1

    # boolean to tell if we found the item
    found = False

    # position where the desired item is located
    positionFound = -1

    while first <= last and not found:

        # we calculate the middle position in the array
        # depending on the current values of first and last
        middle = (first + last)//2

        # we verify if the item is located in middle position
        if list[middle] == item:

            # if it is found, we notify it through found variable
            found = True

            # save the item's position
            positionFound = middle
        else:

            # if it is not found, we must update the current bound values

            # if the desired item is lesser than the current item in
            # middle position, then we must move the superior bound
            # to just before middle value. If the desired item is greater
            # than the current item in middle position, then we must move
            # the inferior bound to just after middle value.
            if item < list[middle]:
                last = middle - 1
            else:
                first = middle + 1
    
    # return if item is found and the position where it is located
    return found, positionFound

# Testcases
print(binSearch([1, 4, 6, 9, 11, 17, 89, 91, 105], 17))
print(binSearch([1, 4, 6, 9, 11, 17, 89, 91, 105], 1))
print(binSearch([1, 4, 6, 9, 11, 17, 89, 91, 105], 88))

