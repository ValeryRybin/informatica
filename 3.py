a=input().split()
for i in range(len(a)):
    c=a[0:i]+a[i+1:len(a)]
    if a[i] not in c: 
        print(a[i])