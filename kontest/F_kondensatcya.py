from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def _dfs(self, v, visited, stack):
        dfs_stack = [(v, False)]  
        while dfs_stack:
            node, process = dfs_stack.pop()        
            if process:
                stack.append(node) 
                continue            
            if visited[node]:
                continue      
            visited[node] = True
            dfs_stack.append((node, True))
            for neighbor in reversed(self.graph[node]):
                if not visited[neighbor]:
                    dfs_stack.append((neighbor, False))

    def _transpose(self):
        transposed_graph = Graph(self.V)
        for node in self.graph:
            for neighbor in self.graph[node]:
                transposed_graph.add_edge(neighbor, node)
        return transposed_graph

    def _fill_order(self, visited, stack):
        for i in range(self.V):
            if not visited[i]:
                self._dfs(i, visited, stack)

    def _dfs_util(self, v, visited, component):
        stack = [v]
        visited[v] = True
        while stack:
            node = stack.pop()
            component.append(node)
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)

    def kosaraju_scc(self):
        stack = deque()
        visited = [False] * self.V

        self._fill_order(visited, stack)

        transposed_graph = self._transpose()

        visited = [False] * self.V
        scc_list = []

        while stack:
            node = stack.pop()
            if not visited[node]:
                component = []
                transposed_graph._dfs_util(node, visited, component)
                scc_list.append(component)

        return scc_list

    def build_condensed_graph(self):
        sccs = self.kosaraju_scc()
        scc_map = {v: i for i, scc in enumerate(sccs) for v in scc}
        condensed = Graph(len(sccs))
        
        for v in self.graph:
            for neighbor in self.graph[v]:
                if scc_map[v] != scc_map[neighbor]:
                    condensed.add_edge(scc_map[v], scc_map[neighbor])
        
        return condensed, sccs

n, m = map(int, input().split())
g = Graph(n+1)

for i in range(m):
    u, v = map(int, input().split())
    g.add_edge(u, v)

sccs = g.kosaraju_scc()
condensed_graph, sccs = g.build_condensed_graph()

edgesincg = set()
for node in condensed_graph.graph:
    for neighbor in condensed_graph.graph[node]:
        edgesincg.add((node,neighbor))
print(len(edgesincg))
