def prim(graph, start):
    mst = []  
    dist=0
    visited = set([start])  
    edges = [
        (weight, start, neighbor)
        for neighbor, weight in graph[start].items()
    ]
    
    while edges and len(visited) < len(graph):

        min_edge = None
        min_index = -1
        for i, (weight, u, v) in enumerate(edges):
            if min_edge is None or weight < min_edge[0]:
                min_edge = (weight, u, v)
                min_index = i
        weight, u, v = edges.pop(min_index)  
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            dist+=weight
            
            for neighbor, weight in graph[v].items():
                if neighbor not in visited:
                    edges.append((weight, v, neighbor))
        print("УРА")
    
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
print('hjhjhjhjjhjhhjjhjhjhjhj')