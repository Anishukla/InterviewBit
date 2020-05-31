# -*- coding: utf-8 -*-
"""
Determine whether an integer is a palindrome. Do this without extra space.
"""

class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        A = str(A)
        B = A[-1::-1]
        
        if B==A:
            return 1
        
        else:
            return 0