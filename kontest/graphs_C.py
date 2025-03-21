def bellman_ford(n,m):
    INF = float('inf')
    dist = [INF]*(n+1)
    dist[0] = 0
    edges = []
    conditions = [tuple(map(str,input().split())) for i in range(m)]

    for l, r, k, operation in conditions:
        if operation == '>=':
            edges.append((int(r), int(l) - 1, -int(k)))
        elif operation == '<=':
            edges.append((int(l) - 1, int(r), int(k)))

    for i in range(n):
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return False

    return True
n, m = map(int, input().split())

print("YES" if bellman_ford(n,m) else "NO")






