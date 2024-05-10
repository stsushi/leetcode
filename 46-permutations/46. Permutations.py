class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def recurive(nums,temp,ans): 
            if not nums:
                ans.append(temp)
            for n in range(len(nums)):
                recurive(nums[0:n]+nums[n+1:],temp+[nums[n]],ans)
        temp = []
        recurive(nums,temp,ans)
        return ans
        