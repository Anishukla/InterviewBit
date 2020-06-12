# -*- coding: utf-8 -*-
"""
Given two binary strings, return their sum (also a binary string).
"""

class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
	def addBinary(self, A, B):
        A = int(A, 2)
        B = int(B, 2)
        
        A = A+B
        
        A = bin(A)
        
        return A[2:]