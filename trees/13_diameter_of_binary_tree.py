def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def diameter(root):
    if root is None:
        return 0
    return max(1 + height(root.left) + height(root.right), diameter(root.left), diameter(root.right))
