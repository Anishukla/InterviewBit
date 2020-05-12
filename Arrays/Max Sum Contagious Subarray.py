""" 
Q:- Find the contiguous subarray within an array, A of length N which has the largest sum."""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        val = []
        val.append(A[0])
        req = A[0]
        for i in range(1, len(A)):
            req = max(req+A[i], A[i])
            val.append(req)
            
        res = max(val)
        
        return res

