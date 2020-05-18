"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes 
of the first two lists, and should also be sorted.
"""

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        req = ListNode(None)
        get = req
        while A and B:
            if A.val<=B.val:
                get.next = A
                A = A.next
                
            else:
                get.next = B
                B = B.next
                
            get = get.next
            
        if A:
            get.next = A
            
        elif B:
            get.next = B
            
        return req.next