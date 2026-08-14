# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        stack = [(root, 0, False)]
        seen = { None : 0 }

        while stack:
            node, depth, processed = stack.pop()

            if not node:
                continue
            
            if processed:

                left = seen[node.left] 
                right = seen[node.right] 

                if abs(left - right) > 1: return False
                seen[node] = 1 + max(left, right)
            else:
                stack.append((node, depth, True))
                stack.append((node.right, depth + 1, False))
                stack.append((node.left, depth + 1, False))

        return True

