class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        so_far = []
        seen = set()
        def backtrack():
            if len(so_far) == len(nums):
                ans.append(so_far[:])
            for elem in nums:
                if elem in seen:
                    pass
                else:
                    so_far.append(elem)
                    seen.add(elem)
                    backtrack()
                    so_far.pop()
                    seen.remove(elem)
        backtrack()
        return ans