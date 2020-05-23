"""Given an unsorted integer array, find the first missing positive integer.
Example:
Given [1,2,0] return 3,
[3,4,-1,1] return 2,
[-8, -7, -6] returns 1

Your algorithm should run in O(n) time and use constant space."""


class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        A = sorted(A)
        
        while(len(A)>=1):
            i = 0
            if A[i]<=0:
                A.pop(0)
                
            elif A[i]>0:
                break
         
        if len(A)>0:
            c = 0
            for i in range(len(A)):
                if A[i]!=i+1:
                    return i+1
                elif A[i]==i+1:
                    c = c+1
                    
            if c==len(A):
                return len(A)+1
        
        elif len(A)==0:
            return 1
