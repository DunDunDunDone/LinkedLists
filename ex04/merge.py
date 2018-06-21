from given_code import *

'''x = SinglyList()
for i in range(0, 40, 2):
    x.add_head(Node(i))

y = SinglyList()
for i in range(1, 50, 3):
    y.add_head(Node(i))'''

def merge(train1, train2):
    newtrain = SinglyList()
    if train1.content > train2.content:
        newtrain.add_head(train1)
        train1temp = train1.next
        train1.next = None
        train1 = train1temp
    else:
        newtrain.add_head(train2)
        train2temp = train2.next
        train2.next = None
        train2 = train2temp
    while train1 != None and train2 != None:
        if train1.content > train2.content:
            train1temp = train1.next
            newtrain.add_head(train1)
            train1 = train1temp
        else:
            train2temp = train2.next
            newtrain.add_head(train2)
            train2 = train2temp
    if train2 != None:
        while train2.next != None:
            train2temp = train2.next
            newtrain.add_head(train2)
            train2 = train2temp
    else:
        while train1.next != None:
            train1temp = train1.next
            newtrain.add_head(train1)
            train1 = train1temp
    l = []
    list_head = newtrain.head
    while True:
        l.append(list_head)
        list_head = list_head.next
        if list_head == None:
            break
    l.reverse()
    x = l[0]
    for t in range(len(l)):
        try:
            l[t].next = l[t+1]
        except:
            l[t].next = None
    return x

def print_list(list_head):
    while True:
        print(list_head.content)
        list_head = list_head.next
        if list_head == None:
            break

#print_list(merge(x.head, y.head))
