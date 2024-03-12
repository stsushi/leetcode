class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: 
            return 0
        post_s = '#'.join('^{}$'.format(s))
        center, right = 0,0
        P = [0]*len(post_s)
        for i in range(1,len(post_s)-1):
            P[i] = (right > i) and min(right - i, P[2*center - i])
            while post_s[i + 1 + P[i]] == post_s[i - 1 - P[i]]:
                P[i] += 1
            if i + P[i] > right:
                center, right = i, P[i]+i
        max_s, c = max((n, i) for i, n in enumerate(P))
        return s[(c  - max_s)//2: (c  + max_s)//2]
        