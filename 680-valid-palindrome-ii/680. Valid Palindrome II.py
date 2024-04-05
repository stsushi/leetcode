class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def helper(i,j,canSkip=True):

            while(i < j):
                if s[i]==s[j]:
                    i+=1
                    j-=1
                elif canSkip:
                    return helper(i+1,j,False) or  helper(i,j-1,False) 
                else:
                    return False
            return True
        return helper(0,len(s)-1)