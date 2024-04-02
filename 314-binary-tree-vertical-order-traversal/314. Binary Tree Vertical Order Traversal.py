from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        record = dict()
        queue = deque([(root, 0)])

        while queue:
            curr, currpos = queue.popleft()

            record[currpos] = record.get(currpos, []) + [curr.val]

            if curr.left:
                queue.append((curr.left, currpos - 1))
            if curr.right:
                queue.append((curr.right, currpos + 1))
            

        offset = -1 * min(record.keys())

        return [record[i - offset] for i in range(len(record))]



       