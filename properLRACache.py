class DLinkedListNode:  # Typical Doubly Linked Node points forward and back
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def __str__(self):  # String Method to show as Linked List not needed for algo
        return "[{}:{}] -->".format(self.key, self.val) + str(self.next)


class LRUCache:

    def __init__(self, capacity: int):
        self.dummyhead = DLinkedListNode(0, 0)  # Create Fake Head as Null
        self.dummytail = DLinkedListNode(0, 0)  # Create Fake Tail Node as Null
        self.dummyhead.next = self.dummytail  # Point Head to Tail
        self.dummytail.prev = self.dummyhead  # Point Tail to Head

        self.capacity = capacity  # Keep Track of max size

        self.map = {}  # Map to check if a value is in the list with a 1:1 look up

    def remove_node(self, node: DLinkedListNode) -> None:  # Removes the Node from list
        node.prev.next = node.next
        node.next.prev = node.prev

        pass

    def insert_node_to_front(self, node) -> None:  # Inserts a node to the front
        node_prev = self.dummyhead  # Fake Head (empty)
        node_next = self.dummyhead.next  # Old head of list
        node_prev.next = node  # New head
        node.prev = node_prev  # Points to fake head (empty)
        node.next = node_next  # Points to what was old Head
        node_next.prev = node  # Points back
        return

    # Idea is if a node is used move to the front
    def move_node_to_front(self, node) -> None:
        self.remove_node(node)  # Remove it from its old place
        self.insert_node_to_front(node)  # Move it to the front
        return

    def get(self, key: int) -> int:
        # Here is why i made the map

        # If the value is in the map then you just get the value if not return -1

        if key not in self.map:
            return -1

        node = self.map[key]  # Get the Node

        self.move_node_to_front(node)  # Move the node to the front

        return node.val  # Give the value back

    def put(self, key: int, value: int) -> None:

        # Here I first update the value in the map then move the node to the font

        if key in self.map:
            node = self.map[key]  # Get the node
            node.val = value  # Update the Value

            self.move_node_to_front(node)  # Move it to front
        else:
            # If its not in the map then just make a new node
            node = DLinkedListNode(key, value)
            self.map[key] = node  # Update Map

            self.insert_node_to_front(node)  # Move new node to the front

            if len(self.map) > self.capacity:
                # This is where we check if the list is to big

                # delete the node from the map
                del self.map[self.dummytail.prev.key]

                # Remove Least Recently Used
                self.remove_node(self.dummytail.prev)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
