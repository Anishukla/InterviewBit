# -*- coding: utf-8 -*-
"""
Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai).
'n' vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).

Find two lines, which together with x-axis forms a container, such that the container contains 
the most water.

Your program should return an integer which corresponds to the maximum area of water that
 can be contained ( Yes, we know maximum area instead of maximum volume sounds weird. 
 But this is 2D plane we are working with for simplicity ).
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        i = 0
        area = 0
        j = len(A)-1
        while i<j:
            val = (min(A[j], A[i]))*(j-i)
            area = max(area, val)
            if A[i]>A[j]:
                j = j-1
            else:
                i = i+1
        return area