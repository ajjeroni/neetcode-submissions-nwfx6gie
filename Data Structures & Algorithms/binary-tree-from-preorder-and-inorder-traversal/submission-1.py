# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def build_node(l, r):
            if l > r: return None

            nonlocal preOrder_index

            val = preorder[preOrder_index]
            node = TreeNode(val)
            index = inOrder_map[val]
            preOrder_index += 1

            node.left = build_node(l, index - 1)
            node.right = build_node(index + 1, r)

            return node

        preOrder_index = 0

        inOrder_map = {}
        for i,num in enumerate(inorder):
            inOrder_map[num] = i
        
        return build_node(0, len(inorder) - 1)
