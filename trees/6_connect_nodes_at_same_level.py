class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.rightNode = None

def connectNodes(root):
	if root is not None:
		q = [root, None]
		while q:
			cur_node = q.pop(0)
			
			if cur_node:
				cur_node.rightNode = q[0]
					
				if cur_node.left is not None:
					q.append(cur_node.left)
				if cur_node.right is not None:
					q.append(cur_node.right)
			elif q:
				q.append(None)

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
    connectNodes(root)
    print(root.rightNode)
    print(root.left.rightNode.data)
    print(root.right.rightNode)
    print(root.left.left.rightNode.data)
    print(root.left.right.rightNode.data)
    
