# -*- coding: utf-8 -*-
"""
Given a column title as appears in an Excel sheet, return its corresponding column number.
"""

class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        res = 0
        for i in range(len(A)):  
            res = res*26
            res = res + (ord(A[i]) - ord('A') + 1)
      
        return res