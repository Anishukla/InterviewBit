# -*- coding: utf-8 -*-
"""
Find if Given number is power of 2 or not.
More specifically, find if given number can be expressed as 2^k where k >= 1.
"""

import math

class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        A = int(A)
        if A<2:
            return 0
        else:
            val = math.log2(A)
            req = int(val)
            if val == req:
                return 1
            
            else:
                return 0
