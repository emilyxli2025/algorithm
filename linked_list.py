from enum import Enum

class Sorted(Enum):
    Desc = 'desc'
    Asce = 'asce'


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = ListNode(data)

        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next

        last_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ')
            current_node = current_node.next

        print('None')
    
    def search(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node is None or current_node.data == data:
                return True
            
            current_node = current_node.next
        
        return False
    
    def sort(self, sortby: Sorted = Sorted.Asce):
        if self.head is None :
            return
        
        swapped = True
        while swapped is True:
            current = self.head
            swapped = False
            while current.next is not None:
                if ((sortby == Sorted.Asce and current.data > current.next.data) or
                    (sortby == Sorted.Desc and current.data < current.next.data)):
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                
                current = current.next

linked_list = LinkedList()
for x in [96,7,4,2,5,8,9,24,85]:
    linked_list.append(x)

linked_list.display()

linked_list.sort()
linked_list.display()

linked_list.sort(Sorted.Desc)
linked_list.display()



        
