import matplotlib.pyplot as plt
import math
from heapq import heappop, heappush

def prim_mst(vertices):
    """Алгоритм Прима для построения MST"""
    n = len(vertices)
    if n == 0:
        return []
    
    # Создаем список всех возможных ребер с весами
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = vertices[i]
            x2, y2 = vertices[j]
            distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            edges.append((distance, i, j))
    
    # Алгоритм Прима
    mst = []
    visited = set([0])
    heap = []
    
    # Добавляем все ребра из начальной вершины
    for d, u, v in edges:
        if u == 0:
            heappush(heap, (d, u, v))
    
    while heap and len(visited) < n:
        d, u, v = heappop(heap)
        if v not in visited:
            visited.add(v)
            mst.append((u, v))
            # Добавляем новые ребра
            for d_new, u_new, v_new in edges:
                if v in (u_new, v_new) and (v_new if v == u_new else u_new) not in visited:
                    heappush(heap, (d_new, u_new, v_new))
    
    return mst

def draw_graph(vertices, edges, title="Граф с MST"):
    """Визуализация графа с минимальным остовным деревом"""
    x = [v[0] for v in vertices]
    y = [v[1] for v in vertices]
    
    plt.figure(figsize=(10, 10))
    
    # Рисуем все вершины
    plt.scatter(x, y, color='blue', s=100)
    
    # Подписываем вершины
    for i, (xi, yi) in enumerate(vertices):
        plt.text(xi, yi, str(i), color='red', fontsize=12)
    
    # Рисуем все возможные ребра серым цветом
    for i in range(len(vertices)):
        for j in range(i+1, len(vertices)):
            plt.plot([vertices[i][0], vertices[j][0]], 
                    [vertices[i][1], vertices[j][1]], 
                    'gray', alpha=0.2, linewidth=1)
    
    # Рисуем ребра MST красным цветом
    for u, v in edges:
        plt.plot([vertices[u][0], vertices[v][0]], 
                [vertices[u][1], vertices[v][1]], 
                'red', alpha=0.8, linewidth=2)
    
    plt.title(title)
    plt.xlabel("X координата")
    plt.ylabel("Y координата")
    plt.grid(True)
    plt.show()

# Парсинг входных данных и обработка каждого графа
input_data = """5\n100\n4 0\n10 34\n35 33\n70 73\n85 9\n99 8\n97 38\n99 72\n8 82\n3 95\n3 49\n13 90\n71 22\n29 98\n14 33\n24 1\n92 35\n24 65\n52 26\n46 77\n15 16\n87 66\n42 52\n8 59\n51 2\n23 84\n3 26\n38 66\n58 53\n67 1\n73 69\n5 53\n54 92\n6 100\n3 28\n67 31\n66 11\n14 28\n35 23\n63 24\n22 16\n76 51\n68 31\n86 12\n95 24\n46 49\n4 13\n12 90\n55 88\n59 86\n67 99\n7 57\n99 85\n10 37\n25 99\n69 62\n35 48\n78 28\n80 98\n2 8\n1 18\n63 76\n20 80\n90 13\n36 97\n39 59\n30 35\n62 70\n54 2\n15 31\n78 78\n17 13\n10 71\n27 96\n88 27\n2 85\n39 15\n49 17\n51 99\n65 34\n43 40\n60 56\n50 0\n18 93\n48 20\n6 14\n33 96\n95 25\n96 63\n99 4\n36 85\n22 86\n29 55\n100 51\n98 99\n65 50\n100 90\n68 0\n97 54\n7 63\n130\n86 72\n1 86\n61 52\n43 46\n99 100\n53 78\n37 15\n49 53\n58 31\n46 11\n60 92\n46 75\n7 10\n86 74\n17 51\n47 18\n42 68\n3 79\n23 91\n66 71\n14 97\n6 13\n32 32\n49 82\n25 36\n37 10\n83 7\n37 19\n58 44\n61 95\n42 45\n92 3\n39 94\n86 26\n77 87\n23 86\n85 15\n3 28\n58 92\n27 95\n1 21\n76 24\n34 55\n88 90\n71 28\n3 76\n48 53\n70 20\n59 20\n33 65\n1 60\n79 62\n71 3\n96 87\n90 16\n98 29\n9 0\n69 69\n50 1\n98 50\n32 59\n13 64\n52 80\n25 8\n1 71\n62 57\n11 82\n28 61\n67 10\n95 26\n41 55\n94 70\n69 16\n77 29\n12 92\n8 70\n56 34\n96 18\n65 12\n19 24\n62 59\n42 35\n83 45\n75 4\n23 94\n44 80\n71 64\n9 25\n9 89\n30 99\n58 2\n24 34\n40 30\n60 8\n67 78\n6 37\n69 75\n21 35\n52 13\n35 61\n65 7\n65 71\n8 83\n99 27\n68 76\n76 25\n51 90\n70 12\n74 67\n85 12\n36 37\n19 85\n65 18\n98 33\n97 77\n27 9\n65 2\n53 46\n22 95\n45 42\n57 7\n15 65\n91 69\n53 94\n55 91\n2 55\n34 90\n2 9\n85 80\n40 2\n105\n53 5\n26 85\n49 80\n35 26\n94 5\n3 33\n1 81\n76 38\n51 57\n85 68\n41 28\n90 85\n82 81\n62 78\n33 42\n2 100\n99 60\n58 28\n96 76\n68 72\n16 10\n53 59\n33 90\n1 30\n79 32\n54 12\n76 42\n0 50\n45 82\n52 60\n17 75\n20 37\n32 2\n33 1\n70 84\n66 77\n81 13\n100 48\n1 96\n8 47\n23 81\n3 23\n66 70\n16 23\n48 21\n45 4\n28 52\n66 91\n97 69\n56 68\n92 18\n58 80\n84 44\n81 54\n88 69\n36 40\n97 7\n91 58\n48 96\n84 28\n10 14\n18 61\n17 38\n31 0\n22 61\n9 43\n3 11\n98 56\n59 37\n9 82\n57 76\n32 40\n70 3\n13 100\n73 38\n42 14\n88 66\n74 12\n92 36\n15 8\n83 97\n22 65\n57 96\n64 10\n86 77\n7 86\n16 34\n50 11\n35 56\n47 21\n27 82\n74 78\n85 87\n65 84\n9 31\n3 100\n73 15\n78 11\n36 14\n17 10\n56 26\n20 91\n46 64\n65 77\n13 79\n205\n97 81\n55 11\n41 31\n39 24\n39 33\n18 99\n68 48\n66 60\n76 15\n84 50\n69 95\n78 43\n18 1\n95 68\n35 81\n87 64\n88 29\n99 38\n35 99\n3 79\n86 31\n3 24\n52 8\n2 4\n85 84\n68 13\n5 94\n81 62\n84 61\n81 7\n33 86\n35 28\n17 44\n98 96\n53 18\n81 34\n87 84\n36 11\n77 12\n64 82\n31 24\n36 20\n60 5\n14 81\n85 13\n89 38\n66 18\n58 53\n15 82\n88 88\n56 62\n10 40\n100 62\n2 91\n34 7\n62 87\n46 100\n36 77\n86 81\n43 0\n80 92\n32 73\n13 5\n34 55\n64 68\n8 100\n20 10\n56 9\n19 54\n82 37\n97 19\n58 67\n83 11\n23 24\n6 38\n67 24\n32 2\n68 1\n75 16\n50 26\n64 43\n58 39\n44 83\n68 22\n57 31\n88 46\n4 4\n95 24\n40 33\n80 14\n69 14\n3 23\n67 26\n4 22\n26 52\n10 1\n16 51\n69 32\n95 51\n41 80\n75 82\n32 77\n79 9\n35 73\n47 38\n78 53\n18 66\n10 83\n68 15\n35 82\n91 47\n5 41\n11 36\n56 68\n22 11\n49 29\n40 44\n69 80\n52 73\n8 15\n24 11\n98 79\n61 94\n16 71\n0 84\n2 81\n88 32\n11 93\n23 58\n66 93\n80 55\n9 50\n12 67\n92 66\n23 76\n4 8\n41 2\n79 68\n91 33\n36 97\n61 96\n74 26\n93 48\n74 99\n19 44\n22 6\n65 41\n39 22\n63 23\n3 66\n15 31\n96 59\n12 87\n75 70\n18 45\n42 76\n50 89\n28 86\n22 45\n21 10\n15 24\n32 40\n96 43\n78 62\n43 49\n13 100\n6 94\n21 28\n19 58\n70 76\n17 70\n61 82\n17 24\n37 91\n40 53\n65 82\n75 84\n0 81\n28 97\n45 58\n60 40\n37 100\n31 59\n15 8\n9 47\n15 90\n79 93\n45 24\n33 68\n54 54\n49 67\n80 63\n86 79\n73 79\n15 37\n10 4\n0 3\n29 39\n38 51\n89 41\n32 19\n13 15\n89 50\n11 94\n97 8\n150\n98 37\n4 9\n72 27\n79 42\n36 25\n83 12\n99 63\n2 2\n19 73\n97 38\n38 44\n32 3\n6 48\n22 44\n51 25\n85 91\n38 16\n84 13\n61 45\n61 54\n91 64\n96 60\n14 15\n68 50\n74 66\n39 99\n63 36\n75 65\n48 56\n28 87\n29 52\n85 84\n86 58\n79 19\n0 37\n1 44\n99 49\n45 32\n56 32\n11 9\n72 43\n28 89\n41 83\n6 61\n4 52\n87 68\n99 42\n3 1\n9 51\n91 68\n85 70\n14 83\n59 91\n36 43\n61 42\n39 14\n55 65\n30 45\n60 0\n17 11\n61 17\n24 62\n72 56\n79 71\n10 90\n63 8\n7 82\n49 27\n38 91\n5 66\n78 17\n69 14\n0 61\n60 75\n57 58\n89 99\n2 70\n16 69\n13 82\n1 25\n29 8\n36 56\n66 91\n2 33\n21 22\n84 44\n1 55\n42 8\n61 85\n76 12\n70 97\n93 92\n17 36\n9 87\n47 49\n46 35\n58 64\n97 80\n26 93\n5 6\n12 21\n98 54\n27 76\n24 4\n4 35\n28 20\n73 52\n70 35\n47 42\n76 78\n54 57\n74 35\n82 82\n84 76\n94 1\n9 61\n38 97\n42 67\n45 38\n91 35\n92 34\n21 56\n33 39\n80 22\n35 54\n76 73\n51 83\n91 46\n63 9\n26 17\n43 33\n72 14\n18 13\n67 64\n23 73\n79 93\n8 51\n84 34\n50 11\n33 68\n46 7\n49 76\n31 70\n92 65\n70 80\n22 42\n68 73\n94 92\n85 34\n81 12"""

# Разбор входных данных
lines = input_data.split('\n')
index = 0
num_graphs = int(lines[index])
index += 1

for graph_num in range(1, num_graphs + 1):
    num_vertices = int(lines[index])
    index += 1
    vertices = []
    for _ in range(num_vertices):
        x, y = map(int, lines[index].split())
        vertices.append((x, y))
        index += 1
    
    # Построение MST
    mst_edges = prim_mst(vertices)
    
    # Визуализация
    draw_graph(vertices, mst_edges, f"Граф {graph_num} с MST (n={num_vertices})")