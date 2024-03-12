class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        #2 steps find some way to group and represent similar strings
        #group and return 
        d = collections.defaultdict(list)
        for s in strings:
            ind = []
            prev = ord(s[0])
            for i in range(1,len(s)):
                elem = ord(s[i])
                ind.append((prev-elem)%26)
                prev = elem
            d[tuple(ind)].append(s)
        return list(d.values())