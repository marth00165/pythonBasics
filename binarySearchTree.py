from Node import Node


def driver():
    build_tree()


def build_tree():
    build = input('Build Tree?\n')

    if build == 'yes':
        tree = BST()
        yesno = int(input('Insert more value? 1: yes, 0: no\n'))
        tree = insert_value(tree)
        while yesno == 1:
            tree.printTree()
            yesno = int(input('Insert more value? 1: yes, 0: no\n'))
            tree = insert_value(tree)
    tree.printTree()
    print('thank you for using the BST constructor')


def insert_value(tree):
    x = input('Enter Number to insert\n')
    tree.insert(x)
    print('inserted')
    return tree


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(value)
            else:
                self._insert(value, cur_node.right)
        else:
            print("Value already exists in tree.")

    def find(self, value):
        if self.root:
            is_found = self._find(value, self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value > cur_node.value and cur_node.right:
            return self._find(value, cur_node.right)
        elif value < cur_node.value and cur_node.left:
            return self._find(value, cur_node.left)
        else:
            return False

    def printTree(self):
        buf = []
        output = []
        root = self.root
        if not root:
            print('$')
        else:
            buf.append(root)
            count = 1
            nextCount = 0
            while count > 0:
                node = buf.pop(0)
                if node:
                    output.append(node.value)
                    count -= 1
                else:
                    output.append('$')
                if node and node.left:
                    buf.append(node.left)
                    nextCount += 1
                else:
                    buf.append(None)
                if node and node.right:
                    buf.append(node.right)
                    nextCount += 1
                else:
                    buf.append(None)
                if count == 0:
                    print(output)
                    output = []
                    count = nextCount
                    nextCount = 0
            # print the remaining all empty leaf node part
            for i in range(len(buf)):
                output.append('$')
            print(output)


bstree = BST()

numbers = [4, 2, 8, 5, 10]

for x in numbers:
    bstree.insert(x)

bstree.printTree()

print(bstree.find(4))
print(bstree.find(2))
print(bstree.find(8))
print(bstree.find(5))
print(bstree.find(10))

# driver()
