# -*- coding: utf-8 -*-
"""
Given an array and a value, remove all the instances of that value in the array.
Also return the number of elements left in the array after the operation.
It does not matter what is left beyond the expected length.
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        n, curr = len(A), 0
        for i in range(n):
            if A[i] != B:
                A[curr] = A[i]
                curr += 1
        A = A[:curr]
        return curr