class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_dict = {}
        used = set()
        for index, elem in enumerate(s):
            if elem not in map_dict:
                if t[index] in used:
                    return False
                used.add(t[index])
                map_dict[elem] = t[index]
            else:
                if t[index] != map_dict[elem]:
                    return False
        return True