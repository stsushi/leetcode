class Solution:
    def searchRange(self, nums, target):
        def left(nums, target):
            left = 0
            right = len(nums)
            while(left != right):
                mid = (left+right)//2
                if nums[mid]< target:
                    left = mid+1
                else:
                    right = mid
            return left
        def right(nums,target):
            left = 0
            right = len(nums)
            while(left != right):
                mid = (left+right)//2
                if nums[mid]> target:
                    right = mid
                else:
                    left = mid+1
            return left-1

        left, right = left(nums, target), right(nums, target)
        return (left, right) if left <= right else [-1, -1]