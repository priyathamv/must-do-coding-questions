from collections import deque

class Node:
	def __init__(self, k):
		self.data = k
		self.left = None
		self.right = None

def bottomView(root):
	if root is not None:
		botView = {}
		q	= deque()
		q.append((root, 0))
		while q:
			node, index = q.popleft()
			botView[index] = node.data
			if node.left is not None:
				q.append((node.left, index-1))
			if node.right is not None:
				q.append((node.right, index+1))
		return botView

if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(25)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)

    bottomview = bottomView(root)
    
    for i in sorted(bottomview):
        print(bottomview[i], end=' ')
