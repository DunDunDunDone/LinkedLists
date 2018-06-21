from given_code import *
import random

x = SinglyList()
for i in range(100):
    x.add_head(Node(random.randint(0, 100)))


def sort_asc(unsorted_list):
    newlist = SinglyList()
    unsorted_listtemp = unsorted_list.next
    newlist.head = unsorted_list
    newlist.head.next = None
    unsorted_list = unsorted_listtemp
    
    while True:
        if unsorted_list == None:
            break
        place = newlist.head
        while place != None:
            if unsorted_list.content < place.content:
                break
            else:
                prev = place
                place = place.next
        unsorted_listtemp = unsorted_list.next
        if place == newlist.head:
            newlist.add_head(unsorted_list)
        else:
            prev.next = unsorted_list
            unsorted_list.next = place
        unsorted_list = unsorted_listtemp
    return newlist.head
       
            
            

def print_list(list_head):
    while True:
        print(list_head.content)
        list_head = list_head.next
        if list_head == None:
            break

print_list(sort_asc(x.head))
