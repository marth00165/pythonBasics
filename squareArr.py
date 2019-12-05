arr1 = [5, 10, 20, 30]
arr2 = []
arr3 = []


def square_arr(arr):
    for x in arr:
        arr2.append(pow(x, 2))
    print(arr2)


square_arr(arr1)

print("")


def square_arr_2(n):
    return pow(n, 2)


def answer(arr):
    print(list(map(square_arr_2, arr)))


answer(arr1)



