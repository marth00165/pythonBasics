from collections import defaultdict


class Node(object):
    def __init__(self):
        self.children = defaultdict(Node)
        self.num_usage = 0


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
            node.num_usage += 1

    def find(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.num_usage


contacts = Trie()

contacts.add("Rohit")
contacts.add("Ronald")
contacts.add("Robert")
contacts.add("Marth")
print(contacts.find("Ro"))
print(contacts.find("J"))

