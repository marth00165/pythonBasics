import math


def medianFinder(a1, a):
    a.sort()
    if len(a) == 1:
        return float(a1[0])
    elif len(a) == 2:
        median = float((a1[0] + a1[1]) / 2)
        return median
    elif len(a) > 2 and len(a) % 2 == 0:
        half = math.floor(len(a) / 2)
        return (a[half] + a[half - 1]) / 2
    elif len(a) > 2 and len(a) % 2 != 0:
        half = math.floor(len(a) / 2)
        return float(a[half])
    else:
        return


def runningMedian(a):
    medians = []
    length = len(a)
    z = 0
    while z < length + 1:
        newArr = a[:z]
        medianNumber = medianFinder(a, newArr)
        if medianNumber:
            medians.append(medianNumber)
        z += 1
    return medians


jawn = [87592, 39913, 29754, 7341, 13823, 11277, 38699, 48439, 97628, 7295]

print(runningMedian(jawn))
