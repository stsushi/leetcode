class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(i,j):
            while i < j:
                if s[i] != s[j]:
                    return i, j
                i+=1
                j-=1
            return False, False
        
        i, j = helper(0, len(s)-1)

        if i == False and j == False:
            return True
        else:
            return True if helper(i+1,j) == (False, False) or helper(i, j-1) == (False, False) else False