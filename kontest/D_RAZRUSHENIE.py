class Edge:
    def __init__(self, v, flow, C, rev):
        self.v = v  # Вершина, в которую ведет ребро
        self.flow = flow  # Текущий поток через ребро
        self.C = C  # Пропускная способность ребра
        self.rev = rev  # Индекс обратного ребра в списке смежности целевой вершины

class Graph:
    def __init__(self, V):
        self.adj = [[] for i in range(V)]  # Список смежности для хранения рёбер
        self.V = V  # Количество вершин в графе
        self.level = [0 for i in range(V)]  # Уровни вершин для BFS

    # Добавление ребра в граф
    def addEdge(self, u, v, C):
        # Прямое ребро: поток 0, пропускная способность C
        a = Edge(v, 0, C, len(self.adj[v]))
        # Обратное ребро: поток 0, пропускная способность 0
        b = Edge(u, 0, 0, len(self.adj[u]))
        self.adj[u].append(a)  # Добавляем прямое ребро в список смежности вершины u
        self.adj[v].append(b)  # Добавляем обратное ребро в список смежности вершины v

    # Поиск в ширину (BFS) для определения уровней вершин
    # и проверки возможности отправки потока от s к t
    def BFS(self, s, t):
        for i in range(self.V):
            self.level[i] = -1  # Инициализируем уровни всех вершин как -1

        self.level[s] = 0  # Уровень исходной вершины равен 0

        # Создаем очередь и добавляем в нее исходную вершину
        q = []
        q.append(s)
        while q:
            u = q.pop(0)  # Извлекаем вершину из очереди
            for i in range(len(self.adj[u])):
                e = self.adj[u][i]
                # Если вершина e.v не посещена и поток через ребро меньше пропускной способности
                if self.level[e.v] < 0 and e.flow < e.C:
                    self.level[e.v] = self.level[u] + 1  # Устанавливаем уровень вершины e.v
                    q.append(e.v)  # Добавляем вершину e.v в очередь

        # Если достигли стока, возвращаем True, иначе False
        return False if self.level[t] < 0 else True

    # Поиск в глубину (DFS) для отправки потока после того, как BFS определил уровни
    # flow: текущий поток, который можно отправить
    # start[]: массив для отслеживания следующего ребра для исследования
    # u: текущая вершина
    # t: сток
    def sendFlow(self, u, flow, t, start):
        if u == t:  # Если достигли стока, возвращаем поток
            return flow

        # Перебираем все ребра из текущей вершины
        while start[u] < len(self.adj[u]):
            e = self.adj[u][start[u]]  # Берем следующее ребро
            # Если уровень следующей вершины на 1 больше текущего и поток через ребро меньше пропускной способности
            if self.level[e.v] == self.level[u] + 1 and e.flow < e.C:
                # Находим минимальный поток от u до t
                curr_flow = min(flow, e.C - e.flow)
                temp_flow = self.sendFlow(e.v, curr_flow, t, start)  # Рекурсивно отправляем поток

                # Если поток больше нуля
                if temp_flow and temp_flow > 0:
                    e.flow += temp_flow  # Увеличиваем поток через текущее ребро
                    self.adj[e.v][e.rev].flow -= temp_flow  # Уменьшаем поток через обратное ребро
                    return temp_flow
            start[u] += 1  # Переходим к следующему ребру

    # Функция для нахождения максимального потока в графе
    def DinicMaxflow(self, s, t):
        if s == t:  # Если источник и сток совпадают, возвращаем -1
            return -1

        total = 0  # Инициализируем общий поток

        # Пока существует путь от источника к стоку
        while self.BFS(s, t) == True:
            start = [0 for i in range(self.V + 1)]  # Инициализируем массив start
            while True:
                flow = self.sendFlow(s, float('inf'), t, start)  # Отправляем поток
                if not flow:  # Если поток равен 0, выходим из цикла
                    break
                total += flow  # Добавляем поток к общему потоку

        return total  




t = int(input())
for _ in range(t):
    n = int(input())
    matrix = []
    for _ in range (n):
        line = str(input())
        formatted_line =' '.join([line[i:i+1] for i in range(0, len(line))])
        matrix.append(list(map(int, formatted_line.split())))

    min_cut = float('inf')
    for u in range(1,n):
        shiva = Graph(n)
        for i in range(n):
            for j in range(n):
                shiva.addEdge(i, j, matrix[i][j])
            
        cut_uv = shiva.DinicMaxflow(0, u)
        if cut_uv < min_cut:
            min_cut = cut_uv

    print(min_cut)