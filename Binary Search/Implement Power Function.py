# -*- coding: utf-8 -*-
"""
Implement pow(x, n) % d.

In other words, given x, n and d,

find (xn % d)

Note that remainders on division cannot be negative.
In other words, make sure the answer you return is non negative.
"""

class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        res = 1 % d
        while n > 0:
            if n & 1:  
               res = (res * x) % d
            x = x**2 % d
            n >>= 1
        return res
