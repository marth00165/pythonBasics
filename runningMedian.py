import heapq


def median(minheap, maxheap):
    l1 = len(maxheap)
    l2 = len(minheap)
    total_length = l1 + l2
    if total_length % 2 == 0:
        top1 = -maxheap[0]
        top2 = minheap[0]
        return (top1 + top2) / 2.0
    else:
        if l1 > l2:
            return -maxheap[0]
        else:
            return minheap[0]


def runningMedian(a):
    medians = []
    minheap = []
    maxheap = []

    for num in a:
        if len(maxheap) == 0 or num < -maxheap[0]:
            heapq.heappush(maxheap, -num)
            print("maxheap: ", maxheap)
        else:
            heapq.heappush(minheap, num)
            print("minheap: ", minheap)

        l1 = len(maxheap)
        l2 = len(minheap)
        if l1 - l2 > 1:
            top = heapq.heappop(maxheap)
            heapq.heappush(minheap, -top)
            print("minheap: ", minheap)
        elif l2 - l1 > 1:
            top = heapq.heappop(minheap)
            heapq.heappush(maxheap, -top)
            print("maxheap: ", maxheap)

    return median(minheap, maxheap)



jawn = [1, 2, 3]

print(runningMedian(jawn))
