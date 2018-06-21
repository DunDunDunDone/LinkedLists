from given_code import *

x = SinglyList()
x.head = Node(5)
x.add_head(Node(6))
for i in range(30):
    x.add_head(Node(i))


def add_tail(list_head, val):
    while list_head.next != None:
        list_head = list_head.next
    list_head.next = Node(val)

add_tail(x.head, 16)
        
