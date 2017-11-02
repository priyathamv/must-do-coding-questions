class MinHeap:

    def __init__(self):
        self.heapList = [0]
        self.heapSize = 0

    def insert(self, k):
        self.heapList.append(k)
        self.heapSize += 1
        newIndex = self.heapSize
        self.percUp(newIndex)

    def percUp(self, newIndex):
        while newIndex // 2 > 0:
            if self.heapList[newIndex] < self.heapList[newIndex // 2]:
                temp = self.heapList[newIndex]
                self.heapList[newIndex] = self.heapList[newIndex // 2]
                self.heapList[newIndex // 2] = temp
            newIndex = newIndex // 2

    def delMin(self):
        self.heapList[1] = self.heapList[self.heapSize]
        self.heapList.pop()
        self.heapSize -= 1
        self.percDown(1)

    def percDown(self, index):
        while index * 2 <= self.heapSize:
            min_child = self.minChild(index)
            if self.heapList[index] > self.heapList[min_child]:
                temp = self.heapList[min_child]
                self.heapList[min_child] = self.heapList[index]
                self.heapList[index] = temp
            index = min_child

    def minChild(self, index):
        if index * 2 + 1 > self.heapSize:
            return index * 2
        else:
            if self.heapList[index*2] < self.heapList[index*2 + 1]:
                return index * 2
            else:
                return index * 2 + 1

    def buildMinHeap(self, arr):
        self.heapSize = len(arr)
        self.heapList = [0] + arr[:]
        i = len(arr) // 2
        while i > 0:
            self.percDown(i)
            i -= 1

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [int(ele) for ele in input().split()]
    k = int(input())
    minHeap = MinHeap()
    minHeap.buildMinHeap(arr)
    for _ in range(k-1):
        minHeap.delMin()
    print(minHeap.heapList[1])
