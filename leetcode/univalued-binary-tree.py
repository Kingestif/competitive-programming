# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        check = True
        def tree(root, rootval):
            if not root:
                return True

            if root.val != rootval:
                return False

            return tree(root.right, rootval) and tree(root.left,rootval)

        return tree(root, root.val)




        