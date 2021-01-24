import numpy as np
import math


def findprimes(n):  # Uses the sieve of erastosthenes method
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        if (prime[p] == True):

            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    primes = []
    for p in range(2, n + 1):
        if prime[p]:
            primes.append(p)
    return primes


def gcd(a,b): # Euclid's algorithm
    if b == 0:
        return a
    elif a >= b:
        return gcd(b,a % b)
    else:
        return gcd(b,a)


def nullspace(A):
    e = min(len(A), len(A[0]))
    for i in range(e):
        maxi = i
        for k in range(i, len(A)):
            if A[k][i] == 1:
                maxi = k
        # print(f'i={i}')
        # print(f'maxi={maxi}')
        if A[maxi][i] == 1:
            A[maxi], A[i] = A[i], A[maxi]
            for u in range(len(A)):
                if u != i:
                    A[u]=[sum(i)%2 for i in zip([x*A[u][i] for x in A[i]],A[u])]
                    '''
                    for j in range(len(A[0])):
                        A[u][j] = A[u][j] + A[u][i] * A[i][j]
                        A[u][j] = A[u][j] % 2
                    '''

    #print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in A]))
    leadingOnes = []
    for i in range(len(A)):
        oneFound = None
        for j in range(len(A[0])):
            if A[i][j] == 1:
                oneFound = j
                break
        leadingOnes.append(oneFound)
    tempA = []
    tempLeadingOnes = []
    for i in range(len(leadingOnes)):
        if (leadingOnes[i] is not None):
            tempA.append(A[i])
            tempLeadingOnes.append(leadingOnes[i])
    A = tempA
    # print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in A]))
    leadingOnes = tempLeadingOnes
    n = len(leadingOnes)
    for i in range(n):
        for j in range(0, n - i - 1):
            if leadingOnes[j] > leadingOnes[j + 1]:
                leadingOnes[j], leadingOnes[j + 1] = leadingOnes[j + 1], leadingOnes[j]
                A[j], A[j + 1] = A[j + 1], A[j]
    for i in range(len(A)):
        j = leadingOnes[i]
        for k in range(len(A)):
            if k != i:
                A[k] = [sum(i) % 2 for i in zip([x * A[k][j] for x in A[i]], A[k])]
                '''
                for l in range(len(A[0])):
                    A[k][l] += A[k][j] * A[i][l]
                    A[k][l] = A[k][l] % 2
                '''
    ns = []
    for i in range(len(A[0])):
        if i not in leadingOnes:
            nsvector = [0] * len(A[0])
            for j in range(len(leadingOnes)):
                if A[j][i] == 1:
                    nsvector[leadingOnes[j]] = 1
            nsvector[i] = 1
            ns.append(nsvector)
    #print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in A]))

    return ns


#N = 12265258567931
#N = 39199007823998693533
N= 54892839618017 #Used this because the original number was taking way too long.
Y = math.exp(math.sqrt(math.log(N) * (math.log(math.log(N)))))
B = math.exp((1 / math.sqrt(2)) * math.sqrt(math.log(N) * (math.log(math.log(N)))))
print(Y)
print(B)
print(math.pi * B)

alist = range(math.floor(math.sqrt(N)) + 1, int(math.floor(math.sqrt(N)) + 1 + Y + 1))

ai = []
primes = findprimes(int(B))
mod2matrix=[]
clist=[]
#bsmoothcount = 0

for a in alist:
    binaries=[]
    ci = pow(a, 2, N)
    corig = ci
    for i in range(len(primes)):
        k = 0
        while (ci % primes[i]) == 0:
            k = k + 1
            ci = ci / primes[i]
        k=k%2
        binaries.append(k)
    if ci == 1:
        #bsmoothcount += 1
        ai.append(a)
        clist.append(corig)
        mod2matrix.append(binaries)


mod2matrix = np.array(mod2matrix).T.tolist()
ns = nullspace(mod2matrix)
factor = 0
for nsvector in ns:
    a = 1
    b = 1
    numexp = []
    for i in range(len(nsvector)):
        if nsvector[i] == 1:
            e=ai[i]
            a = a*ai[i]
            b = b * pow(ai[i], 2, N)
    b = math.isqrt(b)
    #print(a - b)
    factor = gcd(N, a - b)
    if factor != 1 and factor != N and N % factor == 0:
        print(f'{factor} is a factor of N.')
        break
    else:
        print("That didn't work. Trying a new vector!")
