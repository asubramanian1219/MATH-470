import math
import time

n = 1477989791979395596253008425632285999860415010817696638746944786463917339641422937228418383316739449
fin = 0
p = n - 1
while (p % 2 == 0):
    p = p // 2
    fin += 1
# print(fin)
# print(p)
#p = int(p)

found = 0
wits = range(2, math.floor(2 * math.log(n) ** 2) + 1) #witnesses
start=time.time()
prime=0
for a in wits:
    prime = 0
    x=pow(a,p,n)
    if(x==1 or x == n-1):
        continue
    else:
        for k in range(1,fin):
            x=pow(a,p*2**k,n)
            if(x==n-1):
                prime=1
                break
        if prime==1:
            continue
        else:
            print(str(a)+" is a witness for compositeness")
            break
if prime==1:
    print("The number is prime.")
finish=time.time()
print("That took "+str(finish-start)+" seconds.")