arr_jawn = ['Deidara', 'Kisame', 'Itachi']


def deli_counter(arr):
    if len(arr) == 0:
        print("There is no-one in Line")
        take_number(arr)

    else:
        print(f'There are {len(arr)} people in line...')
        take_number(arr)

def take_number(arr):
    name = input('Enter Name to take a number: ')
    arr.append(name)
    x = (arr.index(name) + 1)
    print(f'{name} is #{x} in line!')


deli_counter(arr_jawn)
