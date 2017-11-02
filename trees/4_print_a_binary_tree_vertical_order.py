from collections import deque

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def verticalOrder(root):
	if root is not None:
		verticalMap = {}
		q	= deque()
		q.append((root, 0))
		
		while q:
			node, index = q.popleft()
			
			if index in verticalMap:
				verticalMap[index].append(node.data)
			else:
				verticalMap[index] = [node.data]
			
			if node.left is not None:
				q.append((node.left, index-1))
			if node.right is not None:
				q.append((node.right, index+1))
				
		return verticalMap
		
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

    verticalMap = verticalOrder(root)
    
    for i in sorted(verticalMap):
    	for ele in verticalMap[i]:
    		print(ele, end=" ")
    	print("$", end="")
