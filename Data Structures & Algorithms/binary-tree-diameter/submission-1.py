# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def traversal(node):
            nonlocal path
            if not node: return 0

            left = traversal(node.left)
            right = traversal(node.right)
            
            path = max(path, left + right)
            return 1 + max(left, right)
        
        path = 0
        traversal(root)
        return path