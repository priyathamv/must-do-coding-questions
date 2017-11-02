class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def maxPathSum(root):
	if root is None:
		return 0
	
	l = max(0, maxPathSum(root.left))
	r = max(0, maxPathSum(root.right))
	
	# Max sum path with atmost one child of root
	max_single = max(max(l, r) + root.data, root.data)
	
	max_top = max(max_single, l + r + root.data)
	
	maxPathSum.res = max(max_single, max_top)
	
	return max_single

root = Node(10)
root.left = Node(2)
root.right   = Node(10)
root.left.left  = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left   = Node(3)
root.right.right.right  = Node(4)
maxPathSum(root)
print(maxPathSum.res)
