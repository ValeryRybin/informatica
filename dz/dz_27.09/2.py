import numpy as np

N = int(input())
M = 2
matrix = np.eye(N, M)
print(matrix)

n = int(input())
m = int(input())
print(n,m)
matrix = []
for i in range(0,m):
    matrix.append([])
    for j in range(0,n):
        matrix[i].append(0)
        matrix[i][j] = int(input())
print(matrix)
