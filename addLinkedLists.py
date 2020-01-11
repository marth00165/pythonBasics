class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    number1 = ""
    number2 = ""
    x = 0
    current = l1
    current2 = l2

    while x == 0:
        if current:
            number1 += str(current.val)
            current = current.next
        else:
            number1 = number1[::-1]
            x = 1

    x = 0

    while x == 0:
        if current2:
            number2 += str(current2.val)
            current2 = current2.next
        else:
            number2 = number2[::-1]
            x = 1

    answer = str(int(number1) + int(number2))[::-1]
    length = len(answer)

    answerList = ListNode(answer[0])
    current = answerList
    for element in answer[1:length]:
        current.next = ListNode(element)
        current = current.next

    return answerList


list1 = ListNode(2)
list1.next = ListNode(4)
list1.next.next = ListNode(3)

list2 = ListNode(5)
list2.next = ListNode(6)
list2.next.next = ListNode(4)


print(addTwoNumbers(list1, list2))
