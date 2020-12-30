# node in-order traversal(LDR)
def traversal(node):
    if not node:
        return
    traversal(node.lchild)
    print(node.value, end=' ')
    traversal(node.rchild)


# insert node
def insert(root, value):
    if not root:
        return Node(value)
    if value < root.value:
        root.lchild = insert(root.lchild, value)
    elif value > root.value:
        root.rchild = insert(root.rchild, value)
    return root


# delete node
def delete(root, value):
    if not root:
        return None
    if value < root.value:
        root.lchild = delete(root.lchild, value)
    elif value > root.value:
        root.rchild = delete(root.rchild, value)
    else:
        if root.lchild and root.rchild:  # degree of the node is 2
            target = root.lchild  # find the maximum node of the left subtree
            while target.rchild:
                target = target.rchild
            root = delete(root, target.value)
            root.value = target.value
        else:  # degree of the node is [0|1]
            root = root.lchild if root.lchild else root.rchild
    return root
