class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [None] * (4 * self.n)
        self.build(data, 0, 0, self.n - 1)

    def build(self, data, node, start, end):
        if start == end:
            # лист дерева, сохраняем значение и его частоту
            self.tree[node] = {data[start]: 1}  # {значение: частота}
        else:
            mid = (start + end) // 2
            self.build(data, 2 * node + 1, start, mid)
            self.build(data, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def merge(self, left, right):
        # объединяем два словаря, считая частоту
        result = left.copy()
        for key, value in right.items():
            if key in result:
                result[key] += value
            else:
                result[key] = value
        return result

    def query(self, L, R):
        return self._query(0, 0, self.n - 1, L, R)

    def _query(self, node, start, end, L, R):
        if R < start or end < L:  # Текущий сегмент вне запрашиваемого диапазона
            return {}
        if L <= start and end <= R:  # Текущий сегмент полностью в диапазоне
            return self.tree[node]
        
        mid = (start + end) // 2
        left_result = self._query(2 * node + 1, start, mid, L, R)
        right_result = self._query(2 * node + 2, mid + 1, end, L, R)
        
        # Объединяем результаты
        return self.merge(left_result, right_result)


def most_frequent_count(segment_tree, queries):
    results = []
    for i, j in queries:
        frequency_map = segment_tree.query(i - 1, j - 1)  # Приводим к 0-индексации
        if frequency_map:
            most_frequent = max(frequency_map.values())
            results.append(most_frequent)
        else:
            results.append(0)  # Если нет элементов
    return results


def main():
    t = int(input())
    output = []
    
    for _ in range(t):
        n, q = map(int, input().split())
        data = list(map(int, input().split()))
        queries = [tuple(map(int, input().split())) for _ in range(q)]

        segment_tree = SegmentTree(data)
        results = most_frequent_count(segment_tree, queries)
        output.extend(results)

    print("\n".join(map(str, output)))