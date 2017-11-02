prev = head = None

def convert(root):
    global head, prev
    if root is None:
        return None
    else:
        convert(root.left)
        if prev is None:
            head = root
        else:
            root.left = prev
            prev.right = root
        prev = root
        convert(root.right)
    return head

def BTToDLL(root):
    global head, prev
    head, prev = None, None
    return convert(root)
