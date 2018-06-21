from given_code import *

x = SinglyList()
for i in range(30):
    x.add_head(Node(i))

def remove(list_head, val):
    if list_head != None:
        if list_head.content == val:
            list_head.content = list_head.next.content
            list_head.next = list_head.next.next
        else:
            while list_head.next.content != val and list_head.next != None:
                list_head = list_head.next
            if list_head.next.content == val:
                list_head.next = list_head.next.next

remove(x.head, 25)
