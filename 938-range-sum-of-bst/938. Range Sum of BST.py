# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        if not root: return 0
        if root.val >= low and root.val <= high: result+=root.val
        if root.val > low: result += self.rangeSumBST(root.left, low, high)
        if root.val < high: result += self.rangeSumBST(root.right, low, high)
        return result