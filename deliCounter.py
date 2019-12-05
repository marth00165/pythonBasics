arr_jawn = ['Deidara', 'Kisame', 'Itachi']


def deli_counter(arr):
    if len(arr) == 0:
        print("There is no-one in Line")
        name = input('Enter Name to take a number: ')
        arr.append(name)
        take_number(arr, name)
    else:
        print(f'There are {len(arr)} people in line...')
        name = input('Enter Name to take a number: ')
        arr.append(name)
        take_number(arr, name)


def take_number(arr, name):
    x = (arr.index(name) + 1)
    print(f'{name} is #{x} in line!')


deli_counter(arr_jawn)
