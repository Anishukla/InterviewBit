"""
Given an array of integers, A of length N, find out the maximum sum sub-array of non 
negative numbers from A.
The sub-array should be contiguous i.e., a sub-array created by choosing the second 
and fourth element and skipping the third element is invalid.
Maximum sub-array is defined in terms of the sum of the elements in the sub-array.

Find and return the required subarray.
"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        i = 0
        maxi = -1
        index = 0
        a = []
        
        while i < len(A):
            while i < len(A) and A[i] < 0:
                i+=1
            l = []
            index = i
            while i < len(A) and A[i] >= 0:   
                l.append(A[i])
                i+=1
            
            if (sum(l) > maxi):
                a = l
                maxi = sum(l)
        
        return a