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

    def insert_at(self,val,position):
        if position < 0:
            raise IndexError("Negative position is not supported.Go to hell!!!")

        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            
            while current is not None and count < position:
                prev_node = current
                current = current.next
                count += 1

            prev_node.next = new_node
            new_node.next = current
            

SLL = Singly_Linked_List()
SLL.append(10)
SLL.append(20)
SLL.append(30)
SLL.append(40)
SLL.append(50)
SLL.append(60)
SLL.insert_at(35, -3)
SLL.traversal()
