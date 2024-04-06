# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        def traversal(root):
            if not root:
                return 
            if low <= root.val <= high:
                nonlocal result
                result+=root.val
            if root.val >= low: 
                traversal(root.left)
            if root.val <= high:
                traversal(root.right)
        traversal(root)
        return result