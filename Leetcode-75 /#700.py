# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(root):
            # nonlocal ans
            if root is None:
                return
            if root.val == val:
                # ans = root
                return root
            elif root.val > val:
                return dfs(root.left)
            else:
                return dfs(root.right)
            # return ans
        # ans = None
        return dfs(root)
        # return ans

