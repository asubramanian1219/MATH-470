# question 2a
import time

p = pow(10, 8) + 7
z = pow(826004485, 19, p)
print("Part A Brute Force")
start = time.time()
for i in range(1, p):
    if pow(5, i, p) == z:
        print(i)
        break
end = time.time()
print("That took " + str(end - start) + " seconds.")
print()

# question 2b
# Had to change primes for B and C to orders of 10^9 to get it to work.
p = pow(10, 9) + 39
z = pow(826004485, 19, p)
print("Part B Brute Force")
start = time.time()
for i in range(1, p):
    if pow(3, i, p) == z:
        print(i)
        break
end = time.time()
print("That took " + str(end - start) + " seconds.")
print()

# question 2c
p = pow(10, 9) + 61
z = pow(826004485, 19, p)
print("Part C Brute Force")
start = time.time()
for i in range(1, p):
    if pow(2, i, p) == z:
        print(i)
        break
end = time.time()
print("That took " + str(end - start) + " seconds.")
