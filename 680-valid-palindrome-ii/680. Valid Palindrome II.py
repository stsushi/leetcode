class Solution:
    def validPalindrome(self, s: str) -> bool:
        # have to make it recursive to save the state
        def verify(i,j, can_skip):
            if i < 0 or j > len(s)-1:
                return False
            while i < j:
                if s[i] != s[j]:
                    if can_skip:
                        return verify(i+1,j,False) or verify(i,j-1, False)
                    else:
                        return False
                else:
                    i+=1
                    j-=1
            return True
        return verify(0,len(s)-1,True)