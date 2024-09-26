import math
n = int(input())
c = 0
g = 0
strk = str(n)+" = "
l=""
def prostoe(p):
    c = 0
    for i in range (2, math.ceil(math.sqrt(p))):
        if p % i == 0: c+=1
    if p == 1: c = 1
    if c == 0: return 1
    else: return 0
     
for i in range (1,n):
    if prostoe(i) == 1 and n%i == 0:
        while(n%i == 0):
            n=n/i
            g+=1
        strk = strk + l +"(" +str(i) + "^" + str(g) + ")"
        g = 0
        l = "*"
print(strk)