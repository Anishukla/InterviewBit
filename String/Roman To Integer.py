# -*- coding: utf-8 -*-
"""
Given a string A representing a roman numeral.
Convert A into integer.

A is guaranteed to be within the range from 1 to 3999.
"""

class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        di = {'I': ['V', 'X'], 'X':['L', 'C'], 'C':['D', 'M']}
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        prev = ''
        for i, l in enumerate(A):
            res += d.get(l)
            if i != 0:
                prev = A[i - 1]
                if prev in di and l in di.get(prev):
                    l = list(di)
                    if l.index(prev) == 0:
                        res = res-2
                    elif l.index(prev) == 1:
                        res = res-20
                    else:
                        res = res-200
        return res