from given_code import *

##x = SinglyList()
##x.head = Node(5)
##x.add_head(Node(6))
##for i in range(30):
##    x.add_head(Node(i))

def print_list(list_head):
    while True:
        print(list_head.content)
        list_head = list_head.next
        if list_head == None:
            break

#main(x.head)
