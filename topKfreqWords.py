import collections
import heapq


def topKFrequent(words, k):
    output = []
    heap = []
    count = collections.Counter(words)

    for key, value in count.items():
        heapq.heappush(heap, (-value, key))

    for _ in range(k):
        output.append(heapq.heappop(heap)[1])

    return output


print(topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
