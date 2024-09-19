a=input().split()
c=0
for i in range(len(a)):
    if a.count(a[i]) > c:
        b=a[i]
    c=max(c, a.count(a[i])) 
print(b)