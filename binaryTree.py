from Node import Node
from queue import Queue


class BinaryTree:
    def _init_(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.pre_order_print(self.root, "")
        elif traversal_type == "inorder":
            return self.in_order_print(self.root, "")
        elif traversal_type == "levelorder":
            return self.level_order_print(self.root, "")
        elif traversal_type == "postorder":
            return  self.post_order_print(self.root, "")
        else:
            print("traversal type " + str(traversal_type) + " is not supported")
            return False

    def pre_order_print(self, start, traversal):
        # Root -> Left => Right
        if start:
            traversal += (str(start.value) + " - ")
            traversal = self.pre_order_print(start.left, traversal)
            traversal = self.pre_order_print(start.right, traversal)
        return traversal

    def in_order_print(self, start, traversal):
        # Left -> Root -> Right
        if start:
            traversal = self.in_order_print(start.left, traversal)
            traversal += (str(start.value) + " - ")
            traversal = self.in_order_print(start.right, traversal)
        return traversal

    def post_order_print(self, start, traversal):
        # Left -> Right -> Root
        if start:
            traversal = self.in_order_print(start.left, traversal)
            traversal = self.in_order_print(start.right, traversal)
            traversal += (str(start.value) + " - ")
        return traversal

    def level_order_print(self, root, traversal):
        # Lowest Value -> Highest Value
        if root is None:
            return

        jawn = Queue()
        jawn.enqueue(root)

        while jawn.length() > 0:
            traversal += str(jawn.peek()) + " - "
            node = jawn.dequeue()

            if node.left:
                jawn.enqueue(node.left)
            if node.right:
                jawn.enqueue(node.right)
        return traversal


# Set up tree:
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)
print("pre order traversal: " + tree.print_tree("preorder"))
print("in order traversal: " + tree.print_tree("inorder"))
print("post order traversal " + tree.print_tree("postorder"))
print("level order traversal: " + tree.print_tree("levelorder"))


