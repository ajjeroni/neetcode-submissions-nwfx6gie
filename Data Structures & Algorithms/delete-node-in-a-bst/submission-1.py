# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def _findMin(node):
            while node and node.left:
                node = node.left
            
            return node

        def _delete(node, key):
            if not node: return None

            if node.val < key:
                node.right = _delete(node.right, key)
            elif node.val > key:
                node.left = _delete(node.left, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    minNode = _findMin(node.right)
                    node.val = minNode.val
                    node.right = _delete(node.right, minNode.val)
            
            return node

        return _delete(root, key)
        



        