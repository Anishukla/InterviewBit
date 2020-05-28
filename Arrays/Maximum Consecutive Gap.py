# -*- coding: utf-8 -*-
"""
Given an unsorted array, find the maximum difference between the successive elements 
in its sorted form.
Try to solve it in linear time/space.
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        if len(A)<2:
            return 0
            
        else:
            A = sorted(A)
            maxgap = 0
            for i in range(1, len(A)):
                val = A[i]-A[i-1]
                if val>maxgap:
                    maxgap = val
                    
        return maxgap