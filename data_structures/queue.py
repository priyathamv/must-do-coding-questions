class Queue:
	def __init__(self):
		self.array = []

	def queue(self, k):
		self.array.insert(0, k)

	def dequeue(self):
		if not self.array:
			return -1
		return self.array.pop()

queueOj = Queue()
queueOj.queue(1)
queueOj.queue(2)
queueOj.queue(3)
print(queueOj.dequeue())
print(queueOj.dequeue())
print(queueOj.dequeue())
print(queueOj.dequeue())
