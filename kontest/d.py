def _max_area (n,k,m):
    map_ = [[0]*k for _ in range(n)]
    max_size = 0 
    map_[0][0]=m[0][0]
    for i in range(n):
        for j in range(k):
            if m[i][j] == 1:
                if i>0 and j>0:
                    map_[i][j]=1+min(map_[i-1][j],map_[i-1][j-1],map_[i][j-1])
                    max_size=max(max_size,map_[i][j])
    return max_size

n,k = map(int, input().split())
m = [[0]*k for _ in range(n)]
for i in range (n):
    d = list(map(int,input().split()))
    for j in range(k):
        m[i][j]=d[j]
print(_max_area(n,k,m))