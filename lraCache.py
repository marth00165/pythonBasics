class DLinkedlistNode:

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def __str__(self):
        return "[{}:{}] -->".format(self.key, self.val) + str(self.next)

class LRUCache(object):

    def __init__(self, capacity: int):

        self.dummyhead = DLinkedlistNode(0, 0)
        self.dummytail = DLinkedlistNode(0, 0)
        self.dummyhead.next = self.dummytail
        self.dummytail.prev = self.dummyhead

        self.capacity = capacity

        self.hashmap = {}

    def __remove_node(self, node: DLinkedlistNode) -> None:

        node.prev.next = node.next
        node.next.prev = node.prev

        pass

    def __insert_node_to_front(self, node) -> None:
        node_prev = self.dummyhead
        node_next = self.dummyhead.next
        node_prev.next = node
        node.prev = node_prev
        node.next = node_next
        node_next.prev = node
        return

    def __move_node_to_front(self, node) -> None:
        self.__remove_node(node)
        self.__insert_node_to_front(node)
        return

    def get(self, key):
        if key not in self.hashmap: return -1
        res = self.hashmap[key].val
        self.__move_node_to_front(self.hashmap[key])

        # print("get{}, {}".format(key, str(self.dummyhead)))

        return res

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:

            node = self.hashmap[key]
            node.val = value
            self.__move_node_to_front(node)

        else:

            node = DLinkedlistNode(key, value)
            self.hashmap[key] = node
            self.__insert_node_to_front(node)

            if len(self.hashmap) > self.capacity:
                del self.hashmap[self.dummytail.prev.key]
                self.__remove_node(self.dummytail.prev)


cache = LRUCache(2)

print(cache.get(2))
cache.put(2, 6)
print(cache.get(1))
cache.put(1, 5)
cache.put(1, 2)
print(cache.get(1))
print(cache.get(2))


