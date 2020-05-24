"""
Reverse digits of an integer.
Example1:
x = 123,
return 321

Example2:
x = -123,
return -321

Return 0 if the result overflows and does not fit in a 32 bit signed integer
"""

class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        A = str(A)
        if A[0]=='-':
            req = A[-1:0:-1]
            while req[0]=='0':
                req = req[1:]
            req = '-'+req
        
            if abs(int(req))>2**32:
                return 0
            return req
            
        else:
            req = A[-1::-1]
            while req[0]=='0':
                req = req[1:]
                
            if int(req)>2**32:
                return 0
            return req
