class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        if len(A) == 0:
            return ''
        first_letter = A[0]
        longest_prefix = ''
        for letter in range(1, len(first_letter)+1):
            prefix = first_letter[0:letter]
            flag = True
            for word in A:
                if (word.startswith(prefix)):
                    pass
                else:
                    flag = False
            if flag:
                longest_prefix = prefix
            else:
                break
        return(longest_prefix)
