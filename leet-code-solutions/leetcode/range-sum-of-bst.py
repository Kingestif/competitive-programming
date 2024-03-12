# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        tsum = 0
        def func(root,tsum):
            if not root:
                return tsum

            if root.val >= low and root.val <= high:
                tsum += root.val
                
            tsum = func(root.left,tsum)
            tsum = func(root.right,tsum)

            return tsum

        return func(root,tsum)