"""
Given an integer array, find if an integer p exists in the array such that the 
number of integers greater than p in the array equals to p.
If such an integer is found return 1 else return -1
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        A = sorted(A)
        for i in range(n):
            if A[i]==len(A)-(i+1) and (i!=(n-1)):
                if A[i+1]>A[i]:
                    return 1
                    
            elif A[i]==len(A)-(i+1) and (i==(n-1)):  
                return 1
                    
        return -1