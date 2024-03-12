from random import choice
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # naive approach sort it and return nlogn, klogn
        # m+n better approach bucket the elements n time to put in buckets m runtime to check buckets and return starting from max->min
        # 1/2n+1/4n...->n best approach quick select n runtime 
        def quickselect(nums, k):
            pivot = choice(nums)
            smaller = []
            bigger = []
            same = []
            for num in nums:
                if num < pivot:
                    smaller.append(num)
                elif num > pivot:
                    bigger.append(num)
                else:
                    same.append(num)
            if len(bigger) >= k:
                return quickselect(bigger,k)
            elif len(same)+len(bigger)< k:
                return quickselect(smaller,k-len(bigger)-len(same))
            else:
                return pivot
        return quickselect(nums,k)