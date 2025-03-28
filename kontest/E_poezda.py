n, e, m = map(int, input().split())
conditions = [list(map(int,input().split())) for i in range(m)]

edges = []
for condition in conditions:
    k = condition[0]
    for i in range(k-1):
            edges.append(condition[2*i+1:2*i+5])
sorted_edges = sorted(edges, key=lambda x: x[1])
INF = float('inf')
time_poyavleniya = [INF]*(n+1)
visited = [0]*(n+1)
time_poyavleniya[1]=0
visited[1]=1
for sorted_edge in sorted_edges:
    if visited[sorted_edge[0]]==1:
        if time_poyavleniya[sorted_edge[0]] <= sorted_edge[1]:
            time_poyavleniya[sorted_edge[2]]=min(sorted_edge[3],time_poyavleniya[sorted_edge[2]])
            visited[sorted_edge[2]]=1
if time_poyavleniya[e] == INF: print(-1)
else: print(time_poyavleniya[e])