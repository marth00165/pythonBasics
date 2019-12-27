from collections import defaultdict


class Node(object):
    def __init__(self):
        self.children = defaultdict(Node)
        self.num_usage = 0


class Trie2:
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


class Trie:
    def __init__(self):
        self.root = {}
        self.total = []

    def add(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['*'] = True

    def find(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        if '*' in node:
            return True
        else:
            return False

    def starts_with(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            # self.total.append(len(node))
            node = node[char]

        return True

    def total_stars(self, word):
        return self.root.get(word) or 0


contacts = Trie()
contacts2 = Trie2()
contacts2.add("Rohit")
contacts2.add("Ronald")
contacts2.add("Robert")
print(contacts2.find("Ro"))  # this finds total occurrences of substring


contacts.add("Hack")
contacts.add("Hackerrank")
contacts.add("Hacking")
contacts.add("Rohit")
contacts.add("Rohald")
contacts.add("Ropon")
print(contacts.find("Rohit"))  # finds if contact exists
print(contacts.starts_with("Roh"))  # this finds if there is a contact starts with substring
print(contacts.total_stars("Hac"))
# print(contacts.total_stars("Hak"))
# print(contacts.root)

