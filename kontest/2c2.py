numbers = list(map(int, input().split()))
newfriends=[]
c=-1
k=0
for i in range (len(numbers)-1):
    for j in range(i,len(numbers)):
        if numbers[j]>c:
            k+=1
            c=numbers[j]            
    newfriends.append(k-1)
    k=0
    c=-1
newfriends.append(0)
print(*newfriends)