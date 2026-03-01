# Given head of a singly linked list. The task is to find the length of the linked list, where length is defined as the number of nodes in the linked list.

# Examples :

# Input: head : 1->2->3->4->5

# Output: 5
# Explanation: Length of the linked list is 5, as there 
# are 5 nodes present in it.

'''
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
'''
class Solution:
    def getCount(self, head):
        # code here
        count = 0
        current = head
        
        while current != None:
            count += 1
            current = current.next
            
        return count