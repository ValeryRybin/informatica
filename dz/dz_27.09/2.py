'''
import numpy as np

N = int(input())
M = 2
matrix = np.eye(N, M)
print(matrix)

n = int(input()) # columns
m = int(input()) # rows
print(n,m)
matrix = []
for i in range(0,m):
    matrix.append([])
    for j in range(0,n):
        matrix[i].append(0)
        matrix[i][j] = int(input())
print(matrix)
'''
import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr)
print(arr.ndim)
print(arr.shape)