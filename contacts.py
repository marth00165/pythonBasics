
class Trie:
    head = {}

    def add(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['*'] = True

    def find(self, word):
        cur = self.head

        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]
        if '*' in cur:
            return True
        else:
            return False


contacts = Trie()

contacts.add("Rohit")
contacts.add("Marth")
print(contacts.find("Rohit"))
print(contacts.find("James"))

