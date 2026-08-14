# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(node1, node2):
            nonlocal res

            if not node1 and not node2:
                return
            
            if (node1 and not node2) or (node2 and not node1):
                res = False
                return
            
            if node1.val != node2.val:
                res = False
                return

            dfs(node1.left, node2.left)
            dfs(node1.right, node2.right)

        res = True
        dfs(p, q)
        return res