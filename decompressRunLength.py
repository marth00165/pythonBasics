def decompressRLElist(nums):
    res_lst = []
    number = ''
    for x in range(0, len(nums), 2):
        number = nums[x + 1]
        f = [number for x in range(nums[x])]
        res_lst.extend(f)
    return res_lst

    answerarr = []

    for i in range(0, len(nums), 2):
        x = 0
        y = i + 1

        while x < nums[i] and y <= len(nums):
            answerarr.append(nums[y])
            x += 1

    return answerarr


numbers = [1, 2, 3, 4]

print(decompressRLElist(numbers))
