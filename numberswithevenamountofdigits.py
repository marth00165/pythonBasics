def findNumbers(nums):
    total = 0;

    for number in nums:
        size = len(str(number))

        if size % 2 == 0:
            total += 1

    return total


print(findNumbers([12, 345, 2, 6, 7896]))

