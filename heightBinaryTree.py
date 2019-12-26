from queue import Queue


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.value < node.value:
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
        self.value = key


r = Node(0)
insert(r, Node(1))
insert(r, Node(2))
insert(r, Node(3))
insert(r, Node(4))
insert(r, Node(5))
# insert(r, Node(6))


def height(root):
    if root is None:
        return -1
    lh = height(root.left)
    rh = height(root.right)

    return 1 + max(lh, rh)


def depth(root):
    if root is None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    return 1 + max(lh, rh)


def levelorder_print(root):
    if root is None:
        return

    jawn = Queue()
    jawn.enqueue(root)

    traversal = ""
    while jawn.length() > 0:
        traversal += str(jawn.peek()) + " - "
        node = jawn.dequeue()

        if node.left:
            jawn.enqueue(node.left)
        if node.right:
            jawn.enqueue(node.right)
    return traversal


print(levelorder_print(r))
print(height(r))  # counts the maximum edges of a binary search tree
print(depth(r))   # counts the maximum nodes of a binary search tree

