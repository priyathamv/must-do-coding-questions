# Recursive
def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def printSpiral(root, i, flag):
    if root is not None:
        if i == 0:
            print(root.data, end=" ")
        if flag:
            printSpiral(root.left, i-1, flag)
            printSpiral(root.right, i-1, flag)
        else:
            printSpiral(root.right, i-1, flag)
            printSpiral(root.left, i-1, flag)

def printSpiralLevelOrder(root):
    flag = False
    for i in range(height(root)):
        printSpiral(root, i, flag)
        flag = not flag
----------------------------------------------------
# iterative
def printSpiralLevelOrder(root):
    stack1 = [root]
    stack2 = []
    
    while stack1 or stack2:
        while stack1:
            cur_node = stack1.pop()
            print(cur_node.data, end=" ")
            if cur_node.right is not None:
                stack2.append(cur_node.right)
            if cur_node.left is not None:
                stack2.append(cur_node.left)
            
        
        while stack2:
            cur_node = stack2.pop()
            print(cur_node.data, end=" ")
            if cur_node.left is not None:
                stack1.append(cur_node.left)
            if cur_node.right is not None:
                stack1.append(cur_node.right)
