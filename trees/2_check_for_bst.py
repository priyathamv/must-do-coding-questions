def maxVal(root):
    if root is None:
        return 0
    return max(root.data, maxVal(root.left), maxVal(root.right))
    
def minVal(root):
    if root is None:
        return 1001
    return min(root.data, minVal(root.left), minVal(root.right))


def isBST(root):
    if root is None:
        return True
    return maxVal(root.left) < root.data and minVal(root.right) > root.data and isBST(root.left) and isBST(root.right)
