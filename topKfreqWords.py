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


def topKFrequency2(words, k):
    freq = {}

    for x in words:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1

    popular_words = sorted(freq.items(), key=lambda item: (-item[-1], item[0]))
    return [x[0] for x in popular_words[:k]]


print(topKFrequency2(["i", "love", "leetcode", "i", "love", "coding"], 2))
print(topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
