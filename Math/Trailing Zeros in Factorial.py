# -*- coding: utf-8 -*-
"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""

class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        val = 5
        res = 0
        while val<=A:
            res = res + A//val
            val = val*5
            
        return res