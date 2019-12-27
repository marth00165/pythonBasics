
resultArr = []


class ContactBook:

    def __init__(self):
        self.m = {}
        self.contacts = []
        self.filter = []

    def add(self, word):
        self.contacts.append(word)
        for i in range(1, len(word) + 1):
            if word[:i] in self.m:
                self.m[word[:i]] += 1
            else:
                self.m[word[:i]] = 1

    def find_substrings(self, word):
        return self.m.get(word) or 0

    def find_contacts_with_ss(self, word):
        self.filter.clear()
        for x in self.contacts:
            if word in x:
                self.filter.append(x)
        return self.filter


rohitsContacts = ContactBook()

rohitsContacts.add("Hack")
rohitsContacts.add("Hackerrank")
rohitsContacts.add("Hackanator")
rohitsContacts.add("HaK")
print(rohitsContacts.find_substrings("Hac"))
print(rohitsContacts.find_contacts_with_ss("Hac"))
rohitsContacts.add("Haku")
rohitsContacts.add("Hakunamon")
rohitsContacts.add("Hakulator")
print(rohitsContacts.find_contacts_with_ss("Hak"))
