class DisjointSet:
    def __init__(self, n):
        """Инициализация структуры непересекающихся множеств"""
        self.parent = list(range(n))  # Каждый элемент сам себе родитель
        self.rank = [0] * n  # Глубина дерева множества
    
    def find(self, u):
        """Находим корень множества, к которому принадлежит u, с применением сжатия пути"""
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Сжатие пути
        return self.parent[u]
    
    def union(self, u, v):
        """Объединяет два множества по рангу"""
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
    def proverochka(self,u,v):
        if self.find(u)==self.find(v): answers.append("YES")
        else: answers.append("NO")
    
n, m, k = map(int, input().split())

djs = DisjointSet(n)
edges_bezdari = [tuple(map(str,input().split())) for i in range(m)]

answers=[]

conditions = [tuple(map(str,input().split())) for i in range(k)]
newconditions = conditions[::-1]
for operation, u , v in newconditions:
    if operation == 'ask': djs.proverochka(int(u)-1,int(v)-1)
    elif operation == 'cut':
        djs.union(int(u)-1,int(v)-1)
print('\n'.join(answers[::-1]))

