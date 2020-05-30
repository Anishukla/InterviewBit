# -*- coding: utf-8 -*-
"""
Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed 
as A^P where P > 1 and A > 0. A and P both should be integers.
"""

import math

class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        if (A==1)  : 
            return 1
       
        for x in range(2,(int)(math.sqrt(A))+1) : 
            y = 2
            p = (int)(math.pow(x, y)) 

            while (p<=A and p>0) : 
                if (p==A) : 
                    return 1
                  
                y = y + 1
                p = math.pow(x, y) 

        return 0