from math import floor, sqrt
import time


def bsgs(g, h, p):
    N = floor(sqrt(p - 1)) + 1

    # dict of powers
    tbl = {pow(g, i, p): i for i in range(N)}

    # Search for an equivalence in the table. Giant step.
    for j in range(N):
        y = (h * pow(g, -j * N, p)) % p
        if y in tbl:
            return j * N + tbl[y]

    # Solution not found
    return None


p = pow(10, 12) + 39
z = pow(826004485, 19, p)

print(bsgs(125222632149,523741445974,p))

print("Part A BSGS")
start = time.time()
print(bsgs(5, z, p))
end = time.time()
print("That took " + str(end - start) + " seconds.")
print()

p = pow(10, 12) + 39
z = pow(826004485, 19, p)

print("part B BSGS")
start = time.time()
print(bsgs(3, z, p))
end = time.time()
print("That took " + str(end - start) + " seconds.")
print(pow(3,938026363695,p)==z)

p = pow(10, 16) + 61
z = pow(826004485, 19, p)

print("Part C BSGS")
start = time.time()
print(bsgs(2, z, p))
end = time.time()
print("That took " + str(end - start) + " seconds.")
print()
