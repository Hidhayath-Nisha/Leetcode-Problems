# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = [(root, 1)]
        while queue:
            root, depth = queue.pop(0)
            if root is None:
                continue
            if root.left is None and root.right is None:
                return depth
            queue.append((root.left, depth + 1))
            queue.append((root.right, depth + 1))
