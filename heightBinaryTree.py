def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


r = Node(50)
insert(r, Node(30))
insert(r, Node(20))
insert(r, Node(40))
insert(r, Node(70))
insert(r, Node(60))
insert(r, Node(80))


def height(root):
    if root is None:
        return 1
    lh = height(root.left)
    rh = height(root.right)

    return 1 + max(lh, rh)


def depth(root):
    if root is None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    return 1 + max(lh, rh)


print(height(r))  # counts the maximum edges of a binary search tree
print(depth(r))   # counts the maximum nodes of a binary search tree

