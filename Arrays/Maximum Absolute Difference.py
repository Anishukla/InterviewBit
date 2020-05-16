"""
You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        l = len(A)
        val = []
        for i in range(l):
            val.append(A[i]+i)
            
        res = max(val)-min(val)
        
        val = []
        for i in range(l):
            val.append(A[i]-i)
            
        res = max(res, (max(val)-min(val)))
            
        return res
