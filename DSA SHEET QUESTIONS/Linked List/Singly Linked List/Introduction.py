class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Singly_Linked_List:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node

        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def traversal(self):
        if self.head == None:
            print('Singly Linked List is empty!!!')

        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end=' ')
                curr = curr.next
            print()

SLL = Singly_Linked_List()
SLL.append(10)
SLL.append(20)
SLL.append(30)
SLL.append(40)
SLL.append(50)
SLL.append(60)
SLL.traversal()
