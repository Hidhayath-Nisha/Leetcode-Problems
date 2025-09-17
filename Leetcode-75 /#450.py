class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def traverse(root):
            if root.left is None:
                return root.val
            else:
                return traverse(root.left)
        def bst(root, val):
            if root is None:
                return None
            if root.val == val:
                if root.left is None and root.right is None:
                    return None
                if root.left is None:
                    return root.right
                if root.right is None:
                    return root.left
                root.val = traverse(root.right) 
                root.right = bst(root.right, root.val)
            elif root.val > val:
                root.left = bst(root.left, val)
            else:
                root.right = bst(root.right, val)
            return root
            
        root = bst(root, key)
        return root
