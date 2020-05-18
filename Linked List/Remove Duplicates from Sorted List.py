"""
Given a sorted linked list, delete all duplicates such that each element appear only once.
For example,
Given 1->1->2, return 1->2.
"""

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        temp = A
        if temp.next==None:
            return A
        else:
            temp = A
            while temp:
                while temp.next!=None and temp.val == temp.next.val:
                    temp.next = temp.next.next
                temp = temp.next
            
            return A