#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a list, rotate the list to the right by k places, where k is non-negative.
For example:
    Given 1->2->3->4->5->NULL and k = 2,
    return 4->5->1->2->3->NULL.
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
    def rotateRight(self, A, B):
        temp = A
        c = 1
        while temp.next:
            c=c+1
            temp=temp.next
        if c==1:
            return A
            
        else:
            newNode = ListNode(None)
            curr = newNode
            
            B = B%c
            req = A
            for i in range(c-B):
                curr.next = req
                req= req.next
                curr = curr.next
                
            curr.next = None
            res = req
            if res:
                while res.next:
                    res = res.next
                res.next = newNode.next
                return req
                
            else:
                req = newNode.next
                return req
        
        
