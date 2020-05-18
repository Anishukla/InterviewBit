"""Given a linked list, remove the nth node from the end of list and return its head.
For example,
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
Note: If n is greater than the size of the list, remove the first node of the list.
"""

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        temp = A
        c = 1
        while temp.next:
            temp = temp.next
            c = c+1
            
        if B>=c:
            A = A.next
            return A
            
        else:
            temp2 = A
            for i in range(c-B-1):
                temp2 = temp2.next
                
            temp2.next = temp2.next.next
            
            return A