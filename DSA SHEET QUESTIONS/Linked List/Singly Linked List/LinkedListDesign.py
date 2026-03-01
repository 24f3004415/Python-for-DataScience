class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if index < 0:
            return -1

        current = self.head
        count = 0
        while current != None:
            if index == count:
                return current.val
            current = current.next
            count += 1
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        if index == 0:
            self.addAtHead(val)
            return
        current = self.head
        count = 0
        while current and count < index - 1:
            current = current.next
            count += 1
        if current:
            new_node = Node(val)
            new_node.next = current.next
            current.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        count = 0
        while current and count < index - 1:
            current = current.next
            count += 1
        if current and current.next:
            current.next = current.next.next


# ---- Local Testing ----
obj = MyLinkedList()

obj.addAtHead(1)        # List: [1]
obj.addAtTail(3)        # List: [1, 3]
obj.addAtIndex(1, 2)    # List: [1, 2, 3]

print(obj.get(0))       # Expected: 1
print(obj.get(1))       # Expected: 2
print(obj.get(2))       # Expected: 3
print(obj.get(3))       # Expected: -1 (out of bounds)

obj.deleteAtIndex(1)    # List: [1, 3]
print(obj.get(1))       # Expected: 3