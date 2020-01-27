def twoSum(nums, target):
    hashTable = {}
    for i in range(len(nums)):
        hashTable[nums[i]] = i

    for i in range(len(nums)):
        if target - nums[i] in hashTable and i != hashTable[target - nums[i]]:
            return [i, hashTable[target - nums[i]]]

    return []


numbers = [2, 7, 11, 15]
target_number = 9

print(twoSum(numbers, target_number))
