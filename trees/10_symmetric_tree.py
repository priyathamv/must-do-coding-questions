class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isSymmetric(root1, root2):
	if root1 is None and root2 is None:
		return True
	if root1 is not None and root2 is not None:
		return root1.data == root2.data and isSymmetric(root1.left, root2.right) and isSymmetric(root1.right, root2.left)
	return False
	
if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(2)
	root.left.left = Node(3)
	root.left.right = Node(4)
	root.right.left = Node(4)
	root.right.right = Node(3)
	print(isSymmetric(root, root))
