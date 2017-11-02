class Queue:
	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	def queue(self, k):
		if not self.stack1:
			self.stack2.append(k)
		else:
			self.stack1.append(k)

	def dequeue(self):
		if len(self.stack1) == 0 and len(self.stack2) == 0:
			return -1

		if not self.stack1:
			while self.stack2:
				self.stack1.append(self.stack2.pop())
			return self.stack1.pop()
		else:
			while self.stack1:
				self.stack2.append(self.stack1.pop())
			return self.stack2.pop()

queueObj = Queue()
queueObj.queue(5)
queueObj.queue(6)
queueObj.queue(7)
print(queueObj.dequeue())
print(queueObj.dequeue())
queueObj.queue(8)
print(queueObj.dequeue())
print(queueObj.dequeue())
