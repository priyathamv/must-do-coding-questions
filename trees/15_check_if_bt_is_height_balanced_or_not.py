class Node:
	def __init__(self, k):
		self.data = k
		self.left = None
		self.right = None
	
def height(root):
	if root is None:
		return 0
	return 1 + max(height(root.left), height(root.right))
	
def checkForBalance(root):
	if root is None:
		return True
	return abs(height(root.left) - height(root.left)) <= 1 and checkForBalance(root.left) and checkForBalance(root.right)

if __name__ == '__main__':
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.left.left.left = Node(7)
        root.left.left.left.left = Node(8)
        root.left.left.left.left.left = Node(9)
        
        
        print(checkForBalance(root))
	
