class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left = [0] *n
        right = [0] *n
        ans = []

        ct = 1
        rt = 1
        for i in range(len(nums)):
            ct*= nums[i]
            rt*=nums[n-1-i]
            left[i] = ct
            right[n-1-i]=rt
        ans.append(right[1])
        for i in range(1,n-1):
            ans.append(left[i-1]*right[i+1])
        ans.append(left[-2])
        return ans