n=int(input())
g=[0]*n
g = list(map(int, input().split()))
if sum(g)%3!=0:
    print("0")
else:
    m=sum(g)//3
    if max(g)>m:
        print("0")
    else:
        g=sorted(g)
        print(g)
        
                
