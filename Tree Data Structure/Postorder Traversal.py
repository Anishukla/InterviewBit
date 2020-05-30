# -*- coding: utf-8 -*-
"""
Given a binary tree, return the postorder traversal of its nodes’ values.

Using recursion is not allowed.
"""


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, A):
        if A is None:
            return
        
        L = []
        s1 = []
        s2 = []
        current = A
        
        s1.append(A)
        
        while s1:
            node = s1.pop() 
            s2.append(node) 
            
            if node.left: 
                s1.append(node.left) 
            if node.right: 
                s1.append(node.right) 
      
        while s2: 
            node = s2.pop() 
            L.append(node.val)
            
        return L
