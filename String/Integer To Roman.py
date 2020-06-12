# -*- coding: utf-8 -*-
"""
Given an integer A, convert it to a roman numeral, and return a string corresponding to its 
roman numeral version.
"""

class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        TL = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        if A == 0:
            return ""
        res = ""
        for val, req in TL:
            if A / val:
                res = res + req*(A//val)
                A = A%val
                continue
        return res