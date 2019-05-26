# Recursive algorithm version done in class
def euclidexRecursive(a, b):
    if a%b == 0:
        return 0,1,b
    else:
        A,B,r = euclidexRecursive(b, a%b)
        return B,A-B*a//b,r

# Test cases
print("---------------- Recursive Version ----------------")
a,b,GCD = euclidexRecursive(102, 18)
print("GCD(%s,%s)=%s | Bezout's coefficients: (%s,%s)" % (102, 18, GCD, a, b))
a,b,GCD = euclidexRecursive(2, 1)
print("GCD(%s,%s)=%s | Bezout's coefficients: (%s,%s)" % (2, 1, GCD, a, b))
a,b,GCD = euclidexRecursive(333, 33)
print("GCD(%s,%s)=%s | Bezout's coefficients: (%s,%s)" % (333, 33, GCD, a, b))
a,b,GCD = euclidexRecursive(49, 35)
print("GCD(%s,%s)=%s | Bezout's coefficients: (%s,%s)" % (49, 35, GCD, a, b))
print("---------------------------------------------------")



# Homework: Extend Euclides Algorithm (iterative version)
def euclidexIterative(a, b):

    # iterates until it is found the base case
    while a%b != 0:

        # saves the current value of b
        tmp = b

        # calculates the next value of b (Tn) depending on current values
        # Tn = Sn-1 - Qn * Tn-1, where Qn = Tn-1/Sn-1
        b = a - a//b * b

        # for the next iteration, now a is b (Sn = Tn-1)
        a = tmp
    
    # return b because when it is found the base case, in the previous iteration
    # b contains the GCD (greatest common divisor)
    return b

# Test cases
print("---------------- Iterative Version ----------------")
GCD = euclidexIterative(102, 18)
print(GCD)
GCD = euclidexIterative(2, 1)
print(GCD)
GCD = euclidexIterative(333, 33)
print(GCD)
GCD = euclidexIterative(49, 35)
print(GCD)
print("---------------------------------------------------")