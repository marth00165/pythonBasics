class LRUCache(object):

    def __init__(self, capacity):
        self.cacheValue = {}
        self.capacity = capacity
        self.cacheObjects = []

    def get(self, key):
        value = self.cacheValue[key]
        print("here")

        for i in range(len(self.cacheObjects)):
            item = self.cacheObjects[i]

            for item_key, item_value in item.items():
                if item_value == value and item_key == key:
                    self.cacheObjects.remove(item)
                    self.cacheObjects.append(item)
        return [value, self.cacheObjects]

    def put(self, key, value):
        self.cacheValue[key] = value

        obj = {}
        obj[key] = value

        if len(self.cacheObjects) == self.capacity:
            self.cacheValue[self.cacheObjects[0][value]] = -1
            self.cacheObjects.remove(self.cacheObjects[0])
            self.cacheObjects.append(obj)

        else:
            self.cacheObjects.append(obj)


cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)

print(cache.get(1))
