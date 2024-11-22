numbers = list(map(int, input().split()))
numbers.reverse()
newfriends=[]
c=0
newfriends.append(c)
for i in range (len(numbers)-1):
    if numbers[i+1]<=numbers[i]: c+=1
    else: pass
    newfriends.append(c)
newfriends.reverse()
print(*newfriends)