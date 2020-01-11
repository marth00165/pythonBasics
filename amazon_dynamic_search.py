from pytrie import StringTrie


def prefixSearch(arr, prefix):
    trie = StringTrie()
    # traverse through list of strings
    # to insert it in trie. Here value of
    # key is itself key because at last
    # we need to return
    for key in arr:
        trie[key] = key
    length = len(prefix) + 1
    for x in range(2, length):
        answer = trie.values(prefix[:x])
        answer.sort()
        print(answer)

        # values(search) method returns list
    # of values of keys which contains
    # search pattern as prefix


arr1 = ['hackerrank', 'hack', 'hacking', ' hazz', 'habbbb', 'hiiiiiiiiii']
prefix1 = "hac"
# create empty trie

prefixSearch(arr1, prefix1)

