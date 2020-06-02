# -*- coding: utf-8 -*-
"""
You are given an array (zero indexed) of N non-negative integers, A0, A1 ,…, AN-1.
Find the minimum sub array Al, Al+1 ,…, Ar so if we sort(in ascending order) that sub array, 
then the whole array should get sorted.
If A is already sorted, output -1.
"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        B = sorted(A)
        L = []
        for i in range(len(A)):
            if A[i]!= B[i]:
                L.append(i)
        
        if len(L)==0:
            res = [-1]
            return res
        
        res = [L[0], L[-1]]
        
        return res