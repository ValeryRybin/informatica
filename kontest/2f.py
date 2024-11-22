x=[]
y=[]
n = int(input().strip())
points = [list(map(int, input().strip().split())) for _ in range(n)]
print(points)
'''n = int(input())
for i in range (n):
    numbers = list(map(int, input().split()))
    x.append(numbers[0])
    y.append(numbers[1])
axis_sym = sum(x)/n

def find(x0,y0):
    c=0
    for i in range (n):
        if x0==x[i] and y0==y[i] : c=1
        else:
            pass
    return c
z=1
for i in range (n):
    if find((2*axis_sym-x[i]),y[i]) : z*=1
    else: z*=0
print(z)'''

def has_symmetry(points):
    if len(points) <= 1:
        return 1
    points_set = set(points)
    x_c = [x for x, y in points]
    x_mean = sum(x_c) / len(x_c)

    for x, y in points:
        mirror_x = x_mean * x_mean - x
        if (mirror_x, y) not in points_set:
            return 0
    
    return 1

n = int(input().strip())
points = [tuple(map(int, input().strip().split())) for _ in range(n)]

print(has_symmetry(points))