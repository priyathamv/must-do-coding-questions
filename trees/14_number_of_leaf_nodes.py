def countLeaves(root):
    if root is None:
        return 0
        
    if root.left is None and root.right is None:
        return 1
    
    return countLeaves(root.left) + countLeaves(root.right)
