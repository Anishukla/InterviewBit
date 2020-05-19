"""
Given a read only array of n + 1 integers between 1 and n, find one number that
 repeats in linear time using less than O(n) space and traversing the stream 
 sequentially O(1) times.
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        di = {}
        for i in range(len(A)):
            if A[i] not in di:
                di.update({A[i]:1})
                
            elif A[i] in di:
                res = A[i]
            
        return res