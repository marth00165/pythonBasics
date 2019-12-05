arr1 = ["fiddleheads","okra","kohlrabi"]
arr2 = ["chicken", "gravy"]

def oxford_comma(arr):
    r2 = []
    if len(arr) == 2:
        print(f'{arr[0]} and {arr[1]}')
    else:
        for i, var in enumerate(arr):
            if i + 1 != len(arr):
                r2.append(f'{var},')
            else:
                r2.append(f'and {var}')
        print(" ".join(r2))


oxford_comma(arr1)
oxford_comma(arr2)



