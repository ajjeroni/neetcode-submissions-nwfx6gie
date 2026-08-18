# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, l_bound, r_bound):
            if not node: return True

            if node.val >= r_bound: return False
            if node.val <= l_bound: return False

            return dfs(node.left, l_bound, node.val) and dfs(node.right, node.val, r_bound)

        return dfs(root, float('-inf'), float('inf'))
