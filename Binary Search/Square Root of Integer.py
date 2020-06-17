# -*- coding: utf-8 -*-
"""
Given an integar A.

Compute and return the square root of A.

If A is not a perfect square, return floor(sqrt(A)).

DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY
"""

import math
class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A==0:
            return A
            
        elif A==1 or A==2 or A==3:
            return 1
            
        else:
            req = A
            while (req/2)**2>A:
                req = req//2
                
            c = req//2
            for i in range(c, 2*(c+1)):
                if i**2 == A:
                    return i
                    
                elif i**2<A and (i+1)**2>A:
                    return i