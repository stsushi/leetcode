from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Length of the input array
        n = len(heights)

        # Initialize previous smaller element and next smaller element lists
        pre = [-1] * n  # Previous smaller element for each bar
        suf = [n] * n   # Next smaller element for each bar

        # Stacks to keep track of the bars
        lft, rgt = [], []

        # Calculate previous and next smaller elements for each bar
        for i in range(n):
            # For the previous smaller element
            while lft and heights[lft[-1]] >= heights[i]:
                # Pop from stack until the current bar is smaller than the stack's top
                lft.pop()
            if lft:
                # If stack is not empty, the current top is the previous smaller element
                pre[i] = lft[-1]
            # Push the current index to the stack
            lft.append(i)
            
            # For the next smaller element, we process the array from the end
            j = n - 1 - i
            while rgt and heights[rgt[-1]] >= heights[j]:
                # Pop from stack until the current bar is smaller than the stack's top
                rgt.pop()
            if rgt:
                # If stack is not empty, the current top is the next smaller element
                suf[j] = rgt[-1]
            # Push the current index to the stack
            rgt.append(j)
        
        # Initialize maximum area
        ans = 0
        # Iterate over all bars to find the maximum area rectangle
        for i in range(n):
            # Calculate the width of the rectangle using pre and suf
            width = suf[i] - pre[i] - 1
            # Calculate the area of the rectangle
            area = width * heights[i]
            # Update maximum area
            ans = max(ans, area)
        # Return the maximum area found
        return ans

# Example usage:
# solution = Solution()
# print(solution.largestRectangleArea([2, 1, 5, 6, 2, 3]))