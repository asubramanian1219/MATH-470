import random
import math


def gcd(a, b):
    if a == 0:
        return b

    return gcd(b % a, a)


n = 137561552222266548750432438817110494804925694036285638641461466275346531844223
i = 1
greatest = 1
random.seed()
a = random.randint(2, n)
while greatest <= 1:
    greatest = gcd(pow(a, math.factorial(i), n) - 1, n)
    i += 1
print("Factors are "+ str(greatest) + " and " + str(n//greatest))
print(str(i - 1)+" GCD steps")

