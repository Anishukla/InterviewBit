# -*- coding: utf-8 -*-
"""
Remove duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element
appears only once and return the new length.

Note that even though we want you to return the new length, make sure to 
change the original array as well in place

Do not allocate extra space for another array, you must do this in place 
with constant memory.
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0: 
            return 0
 
        val = 0
        for i in range(len(A)):
            if A[val] != A[i]:
                val += 1
                A[val] = A[i]
 
        return val + 1