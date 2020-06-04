# -*- coding: utf-8 -*-
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example:
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""

class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        res=str()
        for i in A:
            if(i.isalnum()):
                res = res+i.lower()
        if(res==res[::-1]):
            return 1
        else:
            return 0