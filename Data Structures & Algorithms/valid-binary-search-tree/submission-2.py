# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, float('-inf'), float('inf'))]

        while stack:
            node, l_bound, r_bound = stack.pop()

            if node.val <= l_bound or node.val >= r_bound: return False

            if node.right:
                stack.append((node.right, node.val, r_bound))

            if node.left:
                stack.append((node.left, l_bound, node.val))


        return True