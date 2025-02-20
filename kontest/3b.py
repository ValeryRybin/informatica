n, m = map(int, input().split())
pokupateli = list(map(int, input().split()))
kassa = [0] * m
gotovie_pokupateli = [[] for i in range(m)]
for pokupatel in pokupateli:
    next_kassa = kassa.index(min(kassa))
    kassa[next_kassa] += pokupatel
    gotovie_pokupateli[next_kassa].append(pokupatel)
print(max([sum(x) for x in gotovie_pokupateli]))