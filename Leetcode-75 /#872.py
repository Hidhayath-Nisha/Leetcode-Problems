# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root) -> list:
            if not root:
                return
            if root.left is None and root.right is None:
                output.append(root.val)
            dfs(root.left)
            dfs(root.right)
            return output
        output =[]
        list1 = dfs(root1)
        output = []
        list2 = dfs(root2)
        return list1 == list2


        # -- BFS --- Also not checking Empty tree bca of the given constraints/No order preservation
        # queue1 = deque([root1])
        # queue2 = deque([root2])
        # list1 = []
        # list2 = []
        # while queue1:
        #     currNode = queue1.popleft()
        #     if currNode.left is None and currNode.right is None:
        #         list1.append(currNode.val)
        #     if currNode.left:
        #         queue1.append(currNode.left)
        #     if currNode.right:
        #         queue1.append(currNode.right)
        # while queue2:
        #     currNode = queue2.popleft()
        #     if currNode.left is None and currNode.right is None:
        #         list2.append(currNode.val)
        #     if currNode.left:
        #         queue2.append(currNode.left)
        #     if currNode.right:
        #         queue2.append(currNode.right)
        # print(list1 , list2)
        # return list1==list2
        # output = []
      
