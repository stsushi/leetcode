class SparseVector:
    def __init__(self, nums: List[int]):
        self.dict = {}
        self.length = len(nums)
        for index,elem in enumerate(nums):
            if elem != 0:
                self.dict[index] = elem

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for elem in range(self.length):
            if elem in self.dict and elem in vec.dict:
                ans+= self.dict[elem]*vec.dict[elem]
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)