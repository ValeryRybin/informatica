#import numpy as np
n,m = map(int, input().split())
#print(n,m)
#z = np.zeros((n,m),dtype=int)

z = [[0]*m for _ in range (n)]
#print(z)
z[0][0]=1
for i in range(1,n):
    for j in range(1,m):
        if i-2>=0:
            if j-2>=0:
                z[i][j]=z[i-2][j-1]+z[i-1][j-2]
            else:
                z[i][j]=z[i-2][j-1]
        elif j-2>=0:
            z[i][j]=z[i-1][j-2]
#print(z)
print(z[n-1][m-1])