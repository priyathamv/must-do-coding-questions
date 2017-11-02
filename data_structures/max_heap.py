class MaxHeap:

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
            if self.heapList[newIndex] > self.heapList[newIndex // 2]:
                temp = self.heapList[newIndex]
                self.heapList[newIndex] = self.heapList[newIndex // 2]
                self.heapList[newIndex // 2] = temp
            newIndex = newIndex // 2

    def delMax(self):
        self.heapList[1] = self.heapList[self.heapSize]
        self.heapList.pop()
        self.heapSize -= 1
        self.percDown(1)

    def percDown(self, index):
        while index * 2 <= self.heapSize:
            max_child = self.maxChild(index)
            if self.heapList[index] < self.heapList[max_child]:
                temp = self.heapList[max_child]
                self.heapList[max_child] = self.heapList[index]
                self.heapList[index] = temp
            index = max_child

    def maxChild(self, index):
        if index * 2 + 1 > self.heapSize:
            return index * 2
        else:
            if self.heapList[index*2] > self.heapList[index*2 + 1]:
                return index * 2
            else:
                return index * 2 + 1

    def buildMaxHeap(self, arr):
        self.heapSize = len(arr)
        self.heapList = [0] + arr[:]
        i = len(arr) // 2
        while i > 0:
            self.percDown(i)
            i -= 1

maxHeap = MaxHeap()
# maxHeap.insert(1)
# maxHeap.insert(2)
# maxHeap.insert(3)
# maxHeap.insert(4)
# maxHeap.insert(5)
maxHeap.buildMaxHeap([1, 2, 3, 4, 5])
print(maxHeap.heapList)
maxHeap.delMax()
print(maxHeap.heapList)
