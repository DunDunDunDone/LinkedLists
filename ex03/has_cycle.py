from given_code import *

##x = SinglyList()
##h = Node(700)
##x.add_head(h)
##for i in range(30):
##    y= Node(i)
##    x.add_head(y)
##
##x.add_head(h)

def has_cycle(list_head):
    l = []
    while list_head.next != None:
        if list_head in l:
            return True
        else:
            l.append(list_head)
            list_head = list_head.next
    return False

