n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [x for x, y in points]
axis_sym = sum(x)/n
c=1
b=0
if len(points) <= 1:
    b=2
points_set = set(points)

for x, y in points:
    mirror_x = axis_sym + axis_sym - x
    if (mirror_x, y) not in points_set:
        c=0
if c==0 and b!=2: print("0")
else: print("1")