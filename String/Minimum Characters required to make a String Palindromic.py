# -*- coding: utf-8 -*-
"""
Given an string A. The only operation allowed is to insert characters in the beginning of 
the string.
Find how many minimum characters are needed to be inserted to make the string a palindrome string.
"""

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        B = A[::-1]
        c = 0
        i = 0
        while(B[i:]!=A[:len(A)-i]):
            c = c+1
            i = i+1
            
        return c