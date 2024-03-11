class Solution:
    def platesBetweenCandles(self, s: str, qs: List[List[int]]) -> List[int]:
        n=len(s)
        prefix = [None]*n
        suffix = [None]*n
        candles = [0]*n

        count = 0
        prefix_i = None
        for i, elem in enumerate(s):
            if elem == '|':
                prefix_i = i
            else:
                count+=1
            candles[i] = count
            prefix[i] = prefix_i
        
        suffix_i = None
        for i in range(n-1,-1,-1):
            if s[i] == '|':
                suffix_i = i
            suffix[i] = suffix_i
        ans = []
        for left,right in qs:
            if prefix[right] is not None and suffix[left] is not None and prefix[right] > suffix[left]:
                ans.append(candles[prefix[right]]-candles[suffix[left]])
            else:
                ans.append(0)
        
        return ans