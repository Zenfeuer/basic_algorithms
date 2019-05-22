def euclides(a, b):
    if a%b == 0:
        return b
    else:
        return euclides(b, a%b)

MCD = euclides(18, 12)

print(MCD)
