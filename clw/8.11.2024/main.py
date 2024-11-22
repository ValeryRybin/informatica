import sys

class MaxHeap:

    def init(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1

    # Функция для получения позиции родителя для текущего узла на позиции pos
    def parent(self, pos):
        return pos // 2

    # Функция для получения позиции левого потомка для узла на позиции pos
    def leftChild(self, pos):
        return 2 * pos

    # Функция для получения позиции правого потомка для узла на позиции pos
    def rightChild(self, pos):
        return (2 * pos) + 1

    # Функция, которая возвращает True, если переданный узел является листом
    def isLeaf(self, pos):
        if pos >= (self.size // 2) and pos <= self.size:
            return True
        return False

    # Функция для обмена двух узлов кучи
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    # Функция для упорядочивания кучи (heapify) узла на позиции pos
    def maxHeapify(self, pos):
        # Если узел не является листом и меньше, чем любой из его потомков
        if not self.isLeaf(pos):
            if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or
                self.Heap[pos] < self.Heap[self.rightChild(pos)]):

                # Обмен с левым потомком и упорядочивание левого потомка
                if (self.Heap[self.leftChild(pos)] > 
                    self.Heap[self.rightChild(pos)]):
                    self.swap(pos, self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))

                # Обмен с правым потомком и упорядочивание правого потомка
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))

    # Функция для вставки узла в кучу
    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while (self.Heap[current] > 
               self.Heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)

    # Функция для вывода содержимого кучи
    def Print(self):
        for i in range(1, (self.size // 2) + 1):
            print("РОДИТЕЛЬ : " + str(self.Heap[i]) +
                  " ЛЕВЫЙ ПОТОМОК : " + str(self.Heap[2 * i]) +
                  " ПРАВЫЙ ПОТОМОК : " + str(self.Heap[2 * i + 1]))

    # Функция для удаления и возвращения максимального элемента из кучи
    def extractMax(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.maxHeapify(self.FRONT)
        return popped

if name == "main":
    print('Максимальная куча: ')
    
    maxHeap = MaxHeap(15)
    maxHeap.insert(5)
    maxHeap.insert(3)
    maxHeap.insert(17)
    maxHeap.insert(10)
    maxHeap.insert(84)
    maxHeap.insert(19)
    maxHeap.insert(6)
    maxHeap.insert(22)
    maxHeap.insert(9)

    maxHeap.Print()
    
    print("Максимальное значение: " + str(maxHeap.extractMax()))