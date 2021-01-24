import math


def findprimes(n):  # Uses the sieve of erastosthenes method
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:

        if prime[p]:

            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    primes = []
    for p in range(2, n + 1):
        if prime[p]:
            primes.append(p)
    return primes


N = 12265258567931
#N = 39199007823998693533
Y = math.floor((math.log(N)) ** 3)
B = math.floor((math.log(N)) ** 2)
print(Y)
print(B)
print(math.pi * B)

alist = range(math.floor(math.sqrt(N)) + 1, int(math.floor(math.sqrt(N)) + 1 + Y + 1))

bsmoothcount = 0

for a in alist:
    c = pow(a, 2, N)
    corig = c
    for p in findprimes(int(B)):
        # k = 0
        while (c % p) == 0:
            # k = k + 1
            c = c / p
    if c == 1:
        bsmoothcount += 1
print("There are {} B-smooth numbers.".format(bsmoothcount))
print("B smooth count > pi*B? {}".format(bsmoothcount > math.pi * B))
