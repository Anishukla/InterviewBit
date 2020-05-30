# -*- coding: utf-8 -*-
"""
Given a sorted linked list, delete all nodes that have duplicate numbers,
 leaving only distinct numbers from the original list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        dummy = pre = ListNode(0)
        dummy.next = A
        while A and A.next:
            if A.val == A.next.val:
                while A and A.next and A.val == A.next.val:
                    A = A.next
                A = A.next
                pre.next = A
            else:
                pre = pre.next
                A = A.next
        return dummy.next