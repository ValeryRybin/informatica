def is_bipartite_dfs(graph, node, colors=None, color=0):
    if colors is None:
        colors = {}  # Словарь для хранения цветов вершин
    
    if node in colors:
        return colors[node] == color  # Проверяем, что вершина уже окрашена правильно
    
    colors[node] = color  # Красим текущую вершину в текущий цвет
    
    for neighbor in graph[node]:
        # Рекурсивно проверяем соседей, окрашивая их в противоположный цвет
        if not is_bipartite_dfs(graph, neighbor, colors, 1 - color):
            return False
    
    return True

def check_bipartite(graph):
    colors = {}  # Словарь для хранения информации о цветах вершин
    for node in graph:
        if node not in colors:  # Проверяем каждую компоненту связности
            if not is_bipartite_dfs(graph, node, colors):
                return False  # Если хоть одна компонента не двудольная, возвращаем False
    return True

graph = {}
n = int(input("Введите количество вершин в графе: "))
for i in range(n):
    neighbors = input(f"Введите через пробел номера людей, которые не нравятся человеку или которым он не нравится{i+1}: ")
    if neighbors == '':
        continue
    graph[i+1] = list(map(int, neighbors.split()))
print(graph)
print("Да, можно разделить (true)" if check_bipartite(graph) else "Нет, нельзя разделить (false)")