def levelOrderTraverse(root, level, max_level):
    if root is None:
        return
    
    if max_level[0] < level:
        print(root.data, end=" ")
        max_level[0] = level
    
    levelOrderTraverse(root.left, level+1, max_level)
    levelOrderTraverse(root.right, level+1, max_level)
    
        
def printLeftView(root):
    max_level = [-1]
    levelOrderTraverse(root, i, max_level)
