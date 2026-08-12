# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        stack = [(root, 0, False)]
        diameter = 0
        height = { None:0 }

        while stack:
            node, depth, processed = stack.pop()

            if not node: continue

            if processed:
                left = height[node.left]
                right = height[node.right]
                diameter = max(diameter, left + right)
                depth = max(left, right)
                height[node] = depth + 1
            else:
                stack.append((node, depth, True))
                stack.append((node.right, depth + 1, False))
                stack.append((node.left, depth + 1, False))



        return diameter