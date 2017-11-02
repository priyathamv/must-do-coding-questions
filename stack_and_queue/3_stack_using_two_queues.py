class Queue:
	def __init__(self):
		self.array = []

	def enqueue(self, k):
		self.array.insert(0, k)

	def dequeue(self):
		if not self.array:
			return -1
		return self.array.pop()


class Stack:
	def __init__(self):
		self.queue1 = Queue()
		self.queue2 = Queue()

	def push(self, k):
		self.queue1.enqueue(k)

	def pop(self):
		if len(self.queue1.array) == 0:
			return -1
		while len(self.queue1.array) != 0:
			popELement = self.queue1.dequeue()
			if len(self.queue1.array) != 0:
				self.queue2.enqueue(popELement)
			else:
				temp = self.queue1
				self.queue1 = self.queue2
				self.queue2 = temp
				return popELement


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
stack.push(4)
print(stack.pop())
stack.push(5)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
