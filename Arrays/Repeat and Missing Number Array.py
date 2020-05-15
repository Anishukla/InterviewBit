"""You are given a read only array of n integers from 1 to n.
Each integer appears exactly once except A which appears twice and B which is missing.
Return A and B.
Note: Your algorithm should have a linear runtime complexity."""

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        N = len(A)
        di = {}
        val = 0
        for i in range(len(A)):
            if A[i] not in di:
                val = val+A[i]
                di.update({A[i]:i})
                
            elif A[i] in di:
                req = A[i]
                val = val+A[i]
                
        res = (N*(N+1))//2 - val + req
        
        L = [req, res]
        
        return L