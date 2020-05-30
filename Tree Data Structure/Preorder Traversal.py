# -*- coding: utf-8 -*-
"""
Given a binary tree, return the preorder traversal of its nodes’ values.

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
    def preorderTraversal(self, A):
        if A is None:
            return
        
        s1 = []
        s2 = []
        s1.append(A)
        
        while s1:
            node = s1.pop()
            s2.append(node.val)
            
            if node.right:
                s1.append(node.right)
                
            if node.left:
                s1.append(node.left)
        
        return s2
        
        
