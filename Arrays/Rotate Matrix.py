# -*- coding: utf-8 -*-
"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
You need to do this in place.
"""

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        L = [[0 for i in range(len(A))] for j in range(len(A))] 
        
        for i in range(len(A)):
            for j in range(len(A)):
                L[i][j] = A[len(A)-j-1][i]
        
        return L