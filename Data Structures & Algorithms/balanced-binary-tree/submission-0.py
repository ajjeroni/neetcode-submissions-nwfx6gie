# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #dfs - recursion
        #post-order

        #once we reach leaf we return 0 : no left or right
        balanced = [True]
        

        def dfs(node):
            if not node:
                return 0


            left = dfs(node.left)
            if balanced[0] == False:
                return 0
            right = dfs(node.right)

            if abs(left - right) > 1:
                balanced[0] = False
                return 0
            
            return 1 + max(left, right)

        dfs(root)
        return balanced[0]
            

