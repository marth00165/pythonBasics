class Dequeue(object):
    def __init__(self):
        self.items = []

    def appendLeft(self, item):
        self.items.insert(0, item)

    def append(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def popLeft(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].val

    def length(self):
        return self.size()

    def size(self):
        return len(self.items)
