# -*- coding: utf-8 -*-
"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
return the length of last word in the string.
If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.
"""

class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        B = A.split()
        if len(B)==0:
            return 0
        return len(B[-1])