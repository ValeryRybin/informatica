class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))  
        self.rank = [0] * n  
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

def kruskal(n, edges, hackers):
    edges.sort()  
    ds = DisjointSet(n)  
    total_cost=0
    volume_of_mst=0

    for li, xi, yi in edges:
        if xi in hackers or yi in hackers:
            continue
        if ds.union(xi, yi):
            total_cost+=li
            volume_of_mst+=1

    added_hackers = set() 
    for li, xi, yi in edges:
        if xi in hackers and yi in hackers:
            continue 
        if xi in hackers or yi in hackers:
            u = xi if xi in hackers else yi
            v = yi if xi in hackers else xi
            if u not in added_hackers and ds.find(u) != ds.find(v):
                if ds.union(u, v):
                    total_cost+=li
                    volume_of_mst+=1
                    added_hackers.add(u)

    root = ds.find(0)
    connected = True
    for i in range(1, n):
        if ds.find(i) != root:
            connected = False
            break

    return connected, volume_of_mst, total_cost

conditions = input().split()
n = int(conditions[0])
m = int(conditions[1])
p = int(conditions[2])
hackers = set()
if p > 0:
    hackers = set(int(x)-1 for x in input().split())
edges = []
for _ in range(m):
    xi, yi, li = map(int, input().split())
    xi-=1
    yi-=1
    edges.append((li, xi, yi))

connected, volume_of_mst, total_cost = kruskal(n, edges, hackers)
if connected and volume_of_mst == n-1:
    print(total_cost)
else:
    print("impossible")