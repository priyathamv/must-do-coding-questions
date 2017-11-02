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
                self.heapList[newIndex // 2], self.heapList[newIndex] = self.heapList[newIndex], self.heapList[newIndex // 2]
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
                self.heapList[min_child], self.heapList[index] = self.heapList[index], self.heapList[min_child]
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

minHeap = MinHeap()
minHeap.insert(5)
minHeap.insert(4)
minHeap.insert(3)
minHeap.insert(2)
minHeap.insert(1)
print(minHeap.heapList)
