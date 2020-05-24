"""
Given a positive integer A, return an array of strings with all the integers from 1 to N.
But for multiples of 3 the array should have “Fizz” instead of the number.
For the multiples of 5, the array should have “Buzz” instead of the number.
For numbers which are multiple of 3 and 5 both, the array should have
“FizzBuzz” instead of the number.
"""

class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        L = []
        for i in range(1,A+1):
            if i%15 == 0:
                L.append('FizzBuzz')
            elif i%3 == 0:
                L.append('Fizz')
            elif i%5 == 0:
                L.append('Buzz')
            else:
                L.append(i)
        return L