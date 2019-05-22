# Recursive algorithm version done in class
def euclidexRecursive(a, b):
    if a%b == 0:
        return 0,1,b
    else:
        A,B,r = euclidexRecursive(b, a%b)
        return B,A-B*a//b,r

# Test cases
print("---------------- Recursive Version ----------------")
MCD = euclidexRecursive(102, 18)
print(MCD[2])
MCD = euclidexRecursive(2, 1)
print(MCD[2])
MCD = euclidexRecursive(333, 33)
print(MCD[2])
MCD = euclidexRecursive(49, 35)
print(MCD[2])
print("---------------------------------------------------")

# Homework: Extend Euclides Algorithm (Iterative version)
def euclidexIterative(a, b):

    # iterates until it is found the base case
    while a%b != 0:

        # saves the current value of b
        tmp = b

        # calculates the next value of b (Tn) depending on current values
        # Tn = Sn-1 - Qn * Tn-1
        b = a - a//b * b

        # for the next iteration, now a is b (Sn = Tn-1)
        a = tmp
    
    # return b because when it is found the base case, in the previous iteration
    # b contains the GCD (greates common divisor)
    return b

# Test cases
print("---------------- Iterative Version ----------------")
MCD = euclidexIterative(102, 18)
print(MCD)
MCD = euclidexIterative(2, 1)
print(MCD)
MCD = euclidexIterative(333, 33)
print(MCD)
MCD = euclidexIterative(49, 35)
print(MCD)
print("---------------------------------------------------")