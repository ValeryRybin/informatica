n = int(input())
g=[0]*(n+1)
g[1]=0
for i in range (1,n):
    i+=1
    if i%3==0:
        if i%2==0:
            g[i]=min(g[i//3],g[i//2],g[i-1])+1
        else :
            g[i]=g[i]=min(g[i//3],g[i-1])+1
    elif i%2==0 and i%3!=0:
        g[i]=min(g[i//2],g[i-1])+1
    else :
        g[i]=g[i-1]+1
    i-=1

print(g[n])

#задача с
#сумммируем билеты, проверка на /3, получим сколько билетов нужно каждому.