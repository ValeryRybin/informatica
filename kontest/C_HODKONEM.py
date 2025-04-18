class KuhnAlgorithm:
    def __init__(self, edges, U_size, V_size):
        self.U_size = U_size
        self.V_size = V_size
        self.graph = [[] for _ in range(U_size)]
        
        for u, v in edges:
            self.graph[u].append(v)
        
        self.pair_U = [-1] * U_size  
        self.pair_V = [-1] * V_size  
        
    def dfs(self, u, visited):
        for v in self.graph[u]:
            if not visited[v]:
                visited[v] = True
                if self.pair_V[v] == -1 or self.dfs(self.pair_V[v], visited):
                    self.pair_U[u] = v
                    self.pair_V[v] = u
                    return True
        return False

    def find_max_matching(self):
        matching = 0
        for u in range(self.U_size):
            visited = [False] * self.V_size
            if self.dfs(u, visited):
                matching += 1
        return matching
  
t = int(input())
for i in range(t):
    X_size, Y_size, z = map(int, input().split())
    edges = [(u, v) for u in range(X_size) for v in range(Y_size)]
    dyr_coord = list(map(int, input().split()))
    forbidden = set((dyr_coord[i], dyr_coord[i+1]) for i in range(0, 2*z, 2))
    newedges = [edge for edge in edges if edge not in forbidden]
    kuhn = KuhnAlgorithm(newedges, X_size, Y_size)
    print(kuhn.find_max_matching())