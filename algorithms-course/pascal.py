import time
import sys

sys.setrecursionlimit(5000)

def pascal(n, k):
    if n == 0 or k == 0 or n == k:
        return 1
    return pascal(n-1, k) + pascal(n-1, k-1)

now = time.monotonic()
pascal(5, 3)
end = time.monotonic()
print("n=%s, Execution Time: %s seconds" % (5, end-now))

now = time.monotonic()
pascal(10, 3)
end = time.monotonic()
print("n=%s, Execution Time: %s seconds" % (10, end-now))

now = time.monotonic()
pascal(25, 3)
end = time.monotonic()
print("n=%s, Execution Time: %s seconds" % (20, end-now))

now = time.monotonic()
pascal(50, 3)
end = time.monotonic()
print("n=%s, Execution Time: %s seconds" % (50, end-now))

now = time.monotonic()
pascal(75, 3)
end = time.monotonic()
print("n=%s, Execution Time: %s seconds" % (75, end-now))

now = time.monotonic()
pascal(100, 3)
end = time.monotonic()
print("n=%s, Execution Time: %s seconds" % (100, end-now))

now = time.monotonic()
pascal(150, 3)
end = time.monotonic()
print("n=%s, Execution Time: %s seconds" % (150, end-now))

now = time.monotonic()
pascal(250, 3)
end = time.monotonic()
print("n=%s, Execution Time: %s seconds" % (250, end-now))

now = time.monotonic()
pascal(500, 3)
end = time.monotonic()
print("n=%s, Execution Time: %s seconds" % (500, end-now))

now = time.monotonic()
pascal(750, 3)
end = time.monotonic()
print("n=%s, Execution Time: %s seconds" % (750, end-now))

now = time.monotonic()
pascal(1000, 3)
end = time.monotonic()
print("n=%s, Execution Time: %s seconds" % (1000, end-now))

now = time.monotonic()
pascal(1250, 3)
end = time.monotonic()
print("n=%s, Execution Time: %s seconds" % (1250, end-now))

now = time.monotonic()
pascal(1500, 3)
end = time.monotonic()
print("n=%s, Execution Time: %s seconds" % (1500, end-now))

now = time.monotonic()
pascal(2000, 3)
end = time.monotonic()
print("n=%s, Execution Time: %s seconds" % (2000, end-now))