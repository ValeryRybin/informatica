a=input().split()
c=len(a)
b=""
for i in range(len(a)):
    if a.count(a[i]) == 1:
        b=b+a[i]+" "
print(b)