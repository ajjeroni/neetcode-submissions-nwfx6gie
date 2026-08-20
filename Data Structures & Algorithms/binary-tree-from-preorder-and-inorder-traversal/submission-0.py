# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def construct_tree(l, r):
            nonlocal preorder_index

            if l > r: return None

            val = preorder[preorder_index]
            index = inorder_map[val]
            node = TreeNode(val)
            preorder_index += 1

            node.left = construct_tree(l, index - 1)
            node.right = construct_tree(index + 1, r)

            return node
        
        inorder_map = {}
        for i,num in enumerate(inorder):
            inorder_map[num] = i
        
        preorder_index = 0
        return construct_tree(0, len(inorder) - 1)