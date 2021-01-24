import random
def egcd(a, b):
    if(a<0):
        a+=b
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)




def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None
    elif (x*a)%m==1:
        return x % m
    else:
        return y%m




def ellipticaladdition(A, B, x1, y1, x2, y2, N):
    if x1 == x2 and y1 == y2:
        lambtop = ((3 * x1 ** 2) + A)
        lambBottom = 2 * y1
    else:
        lambtop = y2 - y1
        lambBottom = x2 - x1
    lambInverse = modinv(lambBottom, N)
    if lambInverse is None:
        (gcd,x,y)=egcd(lambBottom,N)
        return gcd #this should be a non-trivial factor of N
    lamb = (lambtop * lambInverse) % N
    nu = pow((y1 - lamb * x1),1,N)
    x3 = pow(((lamb ** 2) - x1-x2),1,N)
    y3 = pow((-(lamb * x3 + nu)),1,N)
    return x3, y3

random.seed()
N = 39199007823998693533
A = random.randint(2,N-1)
x1 = random.randint(2,N-1)
y1 = random.randint(2,N-1)
x2 = x1
y2 = y1
B = ((y1**2)-(x1**3)-A*x1)%N

print(f"A={A}\nB={B}")
print(f"P=({x1}, {y1})")
print(f"Number to be factored is {N}")

# x3=9
# y3=7
ans = 0
for i in range(1, 4000):
    for j in range(0, i):
        if isinstance(ellipticaladdition(A, B, x1, y1, x2, y2, N), tuple):
            (x2, y2) = ellipticaladdition(A, B, x1, y1, x2, y2, N)
        else:
            ans = ellipticaladdition(A, B, x1, y1, x2, y2, N)
            print(f"{ans} is a factor of {N}.")
            break
    if ans != 0:
        break
    x1 = x2
    y1 = y2


