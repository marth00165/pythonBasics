class LRUCache(object):

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cacheValue = {}
        self.cacheObjects = []

    def get(self, key):
        value = 0
        if key in self.cacheValue.keys():
            value = self.cacheValue[key]
        else:
            return -1

        print("here")
        for i in range(len(self.cacheObjects)):
            item = self.cacheObjects[i]
            for item_key, item_value in item.items():
                if item_value == value and item_key == key:
                    self.cacheObjects.remove(item)
                    self.cacheObjects.append(item)
            return [value, self.cacheObjects]

    def put(self, key: int, value: int) -> None:
        self.cacheValue[key] = value
        obj = {}
        obj[key] = value

        for i in range(len(self.cacheObjects)):
            item = self.cacheObjects[i]

            if key in item.keys():
                self.cacheObjects.remove(self.cacheObjects[i])

        if len(self.cacheObjects) == self.capacity:
            item = self.cacheObjects[0]
            for key in item:
                self.cacheValue[key] = -1
            self.cacheObjects.remove(self.cacheObjects[0])
            self.cacheObjects.append(obj)
        else:
            self.cacheObjects.append(obj)

        self.cacheValue[key] = value


cache = LRUCache(2)

print(cache.get(2))
cache.put(2, 6)
print(cache.get(1))
cache.put(1, 5)
cache.put(1, 2)
print(cache.get(1))
print(cache.get(2))


