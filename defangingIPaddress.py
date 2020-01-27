def defangIPaddr(address):
    res = ''
    for i in range(len(address)):
        if address[i] == '.':
            res = res + '[.]'
        else:
            res = res + address[i]
    return res


inputString = "1.1.1.1"


print(defangIPaddr(inputString))
