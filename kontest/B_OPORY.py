import heapq

def prim(graph, start):
    mst = []  
    dist=0
    visited = set([start])  
    edges = [
        (weight, start, neighbor)
        for neighbor, weight in graph[start].items()
    ]
    heapq.heapify(edges)  

    while edges:  
        weight, u, v = heapq.heappop(edges)  
        if v not in visited:
            visited.add(v)  
            mst.append((u, v, weight))  
            dist+=weight
            for neighbor, weight in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (weight, v, neighbor)) 

    return dist

t = int(input())
for i in range (t):
    n = int(input())
    coord = []
    for i in range(n):
        x, y = map(int, input().split())
        coord.append((x, y))
        
    graph = {}
    for i in range(n):
        u = coord[i]
        graph[u] = {}
        x1, y1 = u
        for j in range( n):
            v = coord[j]
            x2, y2 = v
            rastoyanie = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
            graph[u][v] = rastoyanie
    print("{0:.2f}".format(prim(graph,coord[0])))

