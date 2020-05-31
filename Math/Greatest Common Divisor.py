# -*- coding: utf-8 -*-
"""
Given 2 non negative integers m and n, find gcd(m, n)
NOTE : DO NOT USE LIBRARY FUNCTIONS.
"""

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        val = 1
        c = max(A, B)
        d = min(A, B)
        
        if d==0:
            return c
        
        while c%d!=0:
            val = c%d
            c = d
            d = val
            
        return d