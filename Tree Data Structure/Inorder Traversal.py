# -*- coding: utf-8 -*-
"""
Given a binary tree, return the inorder traversal of its nodes’ values.

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
    def inorderTraversal(self, A):
        L = []
        current = A  
        stack = []
        while True: 
          
            if current is not None: 
                stack.append(current) 
                current = current.left
                
            elif(stack): 
                current = stack.pop() 
                L.append(current.val) 
                current = current.right  
  
            else: 
                break
            
        return L
