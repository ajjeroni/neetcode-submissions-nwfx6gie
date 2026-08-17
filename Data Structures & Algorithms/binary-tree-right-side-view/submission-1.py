# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # lets get this bfs
        if not root: return []

        dq = deque()
        dq.append(root)
        res = []

        while dq:
            res.append(dq[-1].val)
            levelLen = len(dq)
            
            for i in range(levelLen):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

        return res
            



















