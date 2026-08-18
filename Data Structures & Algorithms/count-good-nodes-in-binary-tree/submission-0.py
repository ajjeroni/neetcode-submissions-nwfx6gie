# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # we can prolly do bfs - find the max at each level
        dq = deque()
        dq.append((root, -101))
        # root, currMax

        count = 0
        
        while dq:
            dqLen = len(dq)

            for i in range(dqLen):
                node, parentMax = dq.popleft()
                if node.val >= parentMax:
                    count += 1
                parentMax = max(parentMax, node.val)
                
                if node.left:
                    dq.append((node.left, parentMax))
                if node.right:
                    dq.append((node.right, parentMax))
        return count
                