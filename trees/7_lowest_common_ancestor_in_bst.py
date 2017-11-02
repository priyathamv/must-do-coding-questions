def LCA(root, a, b):
    if root is not None:
        if root.data < a and root.data < b:
            return LCA(root.right, a, b)
        
        if root.data > a and root.data > b:
            return LCA(root.left, a, b)
            
        return root
