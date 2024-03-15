# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        def func(total,root):
            if not root:
                return 0
                
            total = total * 10 + root.val
            if not root.left and not root.right:
                return total

            return func(total, root.left) + func(total, root.right)

        return func(0,root)

        