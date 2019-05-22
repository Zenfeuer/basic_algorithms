def euclidexRecursive(a, b):
    if a%b == 0:
        return 0,1,b
    else:
        A,B,r = euclidexRecursive(b, a%b)
        return B,A-B*a//b,r

MCD = euclidexRecursive(18, 12)

print(MCD[2])