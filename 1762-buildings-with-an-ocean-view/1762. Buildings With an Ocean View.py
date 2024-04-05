class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []

        max_h = float("-inf")
        for i in range(len(heights)-1, -1, -1):
            house = heights[i]
            if house > max_h:
                ans.append(i)
                max_h = house
        ans.reverse()
        return ans