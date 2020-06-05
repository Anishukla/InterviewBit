# -*- coding: utf-8 -*-
"""
Given an array ‘A’ of sorted integers and another non negative integer k, 
find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        di ={A[0]:0}
        for i in range(1, len(A)):
            val = A[i] - B
            if val in di:
                return 1
                
            elif val not in di:
                di.update({A[i]:i})
                
        return 0